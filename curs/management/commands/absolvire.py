from django.core.management import BaseCommand
from django.db.models import F

from curs.models import Student

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('max_year', type=int)

    def handle(self, *args, **options):
        print("Here")
        print(options)
        Student.objects.update(an=F('an') + 1)