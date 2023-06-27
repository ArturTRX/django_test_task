import time
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        while True:
            print("Starting import_data script")
            call_command("import_data")
            time.sleep(360)
