from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.db.utils import IntegrityError
from rest_framework_simplejwt.tokens import RefreshToken


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        password = "root"
        username = "root"
        email = "root@root.root"

        User = get_user_model()
        try:
            user = User.objects.create_superuser(username, email, password)
        except IntegrityError:
            user = User.objects.get(username=username)

        token = RefreshToken.for_user(user)
        return str(token.access_token)
