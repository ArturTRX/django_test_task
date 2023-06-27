import asyncio
import aiohttp
from asgiref.sync import sync_to_async

from django.core.management.base import BaseCommand
from core.models import Post, Comment
from django.db import connection


class Command(BaseCommand):
    help = 'Imports posts and comments data from JSONPlaceholder API'

    @staticmethod
    async def fetch_comments(session, post_id):
        async with session.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}/comments') as response:
            return await response.json()

    @staticmethod
    async def fetch_posts(session):
        async with session.get('https://jsonplaceholder.typicode.com/posts') as response:
            return await response.json()

    async def get_data(self):
        async with aiohttp.ClientSession() as session:
            posts = await self.fetch_posts(session)
            tasks = []
            print("Getting posts")
            for post in posts:
                tasks.append(asyncio.ensure_future(self.fetch_comments(session, post['id'])))
            comments = await asyncio.gather(*tasks)
            print("Getting comments")
            return posts, comments

    @sync_to_async
    def reset_sequence(self, model):
        """
        Updating indexes after getting remote data, so we can use AutoFields
        """
        with connection.cursor() as cursor:
            cursor.execute(
                f"SELECT setval(pg_get_serial_sequence('{model._meta.db_table}', 'id'), "
                f"coalesce(max(id), 0) + 1, false) FROM {model._meta.db_table};"
            )

    async def handle_async(self, *args, **kwargs):
        posts, comments_list = await self.get_data()

        for post, comments in zip(posts, comments_list):
            p, _ = await sync_to_async(Post.objects.update_or_create)(
                id=post['id'],
                defaults={
                    'user_id': post['userId'],
                    'title': post['title'],
                    'body': post['body']
                }
            )

            for comment in comments:
                await sync_to_async(Comment.objects.update_or_create)(
                    post=p,
                    id=comment['id'],
                    defaults={
                        'name': comment['name'],
                        'email': comment['email'],
                        'body': comment['body']
                    }
                )
        await self.reset_sequence(Post)
        await self.reset_sequence(Comment)

    def handle(self, *args, **kwargs):
        asyncio.run(self.handle_async(*args, **kwargs))
