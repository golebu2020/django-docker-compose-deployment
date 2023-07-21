"""
Django command to wait for the database to be available
"""

import time
from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

# from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to wait for database."""
    def handle(self, *args, **options):
        """Command entrypoint"""
        self.stdout.write("Waiting for database...")
        db_up = False
        while (db_up == False):
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write("Couldn't connect, waiting for 1 second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database ready!'))
