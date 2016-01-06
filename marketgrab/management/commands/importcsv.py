from django.core.management.base import BaseCommand, CommandError
from marketgrab.models import Data
from datetime import datetime
import csv

class Command(BaseCommand):
    help = 'Input csv data into database'

    def add_arguments(self, parser):
        parser.add_argument('data', nargs='+')

    def handle(self, **options):
        for filename in options['data']:
            with open(filename, 'rb') as csv_file:
                datareader = csv.reader(csv_file, delimiter=',', quotechar='|')
                e = 0
                for row in datareader:
                    data = Data(ticker = filename[:-4], trading_day = row[0], open_price = row[1], high_price = row[2], low_price = row[3], close_price = row[4], volume = int(row[5]), aclose_price = row[6])
                    data.save()
                    self.stdout.write(self.style.SUCCESS('Successfully entered line %s of data' % e))
                    e += 1
        self.stdout.write(self.style.SUCCESS('DONE!'))
