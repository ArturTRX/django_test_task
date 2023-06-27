# Django REST API for JSONPlaceholder

This project implements a REST API using Django and Django REST framework that interacts with the JSONPlaceholder API.

## Requirements

- Python 3
- Django
- Django REST framework
- PostgreSQL
- Docker and docker-compose

## Running the Project

1. Clone the repository
2. Install the requirements by running `pip install -r requirements.txt`
3. Run the docker-compose up with the command `docker-compose up -d`
4. You can use command `docker compose exec -it web ./manage.py init_admin` to obtain access token.
5. The API will be available at `0.0.0.0:8000`

## Available Endpoints

- `GET api/posts/` - Retrieve a list of all posts
- `POST api/posts/` - Create a new post
- `GET api/posts/{id}/` - Retrieve a post by ID
- `PUT api/posts/{id}/` - Update a post by ID
- `DELETE api/posts/{id}/` - Delete a post by ID

- `GET api/comments/` - Retrieve a list of all comments
- `POST api/comments/` - Create a new comment
- `GET api/comments/{id}/` - Retrieve a comment by ID
- `PUT api/comments/{id}/` - Update a comment by ID
- `DELETE api/comments/{id}/` - Delete a comment by ID

## Authentication

The API uses token-based authentication. To retrieve a token, you'll need to create a user and then make a POST request to `api-token-auth/` with the username and password. You can use command `docker compose exec -it web ./manage.py init_admin` to obtain access token.

## Synchronization

The data synchronization with the JSONPlaceholder API is performed by executing the Django command `python manage.py import_data`. 
This could be set up to run periodically using a scheduled task or cron job.
Or with `docker compose exec -it web ./manage.py infinite_polling`