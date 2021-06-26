from django.core.management import BaseCommand
from django.db.models import F

from curs.models import Student

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print("Here")
        Student.objects.update(an=F('an') + 1)