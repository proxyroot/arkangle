from django.core.management.base import BaseCommand, CommandError
from search.models import Cluster


class Command(BaseCommand):
    help = 'Create test data using model save'


    def handle(self, *args, **options):
        data = [
            {"name": "Amazon", "nodes": 1000},
            {"name": "Michigan", "nodes": 2000},
            {"name": "Rhino", "nodes": 500},
            {"name": "Tahoe", "nodes": 420},
        ]
        for item in data:
            cluster = Cluster(**item)
            cluster.save()
            self.stdout.write(self.style.SUCCESS('Successfully created cluster "%s"' % cluster.name))