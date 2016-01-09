from django.core.management.base import BaseCommand, CommandError
from marketgrab.models import Data
from datetime import datetime
from time import mktime, strptime

class Command(BaseCommand):
    help = 'Convert string from trading_day to datetime and add to date'

    def handle(self, **options):
        for row in Data.objects.all():
            day = row.trading_day
            day = datetime.fromtimestamp(mktime(strptime(day, "%Y-%m-%d")))
            row.date = day
            row.save()
            self.stdout.write(self.style.SUCCESS('Saved %s in new row' % row.trading_day))
        self.stdout.write(self.style.SUCCESS('DONE!'))
