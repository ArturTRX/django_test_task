from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

from .models import Post, Comment


class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title='test title', body='test body')

    def test_title_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.title}'
        self.assertEquals(expected_object_name, 'test title')

    def test_body_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.body}'
        self.assertEquals(expected_object_name, 'test body')


