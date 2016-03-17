from django.core.management.base import BaseCommand, CommandError
from marketgrab.models import Data
import datetime
import csv
import urllib2

class Command(BaseCommand):
    help = 'Input csv data into database'

    def add_arguments(self, parser):
        parser.add_argument('-t', '--tickers', nargs='+', required=True)

    def handle(self, **options):
        for t in options['tickers']:
            fromdate = Data.objects.filter(ticker = t).latest('date').date
            m = fromdate.month - 1
            todate = datetime.date.today()
            o = todate.month - 1
            b = fromdate.day
            a = '%02d' % m
            c = fromdate.year
            e = todate.day
            d = '%02d' % o
            f = todate.year

            url = 'http://real-chart.finance.yahoo.com/table.csv?s=%s&a=%s&b=%s&c%s&d=%s&e=%s&f=%s&g=d&ignore=.csv' % ('^'+t, a, b, c, d, e, f)
            response = urllib2.urlopen(url)

            datareader = csv.reader(response, delimiter=',', quotechar='|')
            e = 0
            self.stdout.write(self.style.SUCCESS('datareader rows: %s' % sum(1 for row in datareader)))

            self.stdout.write(self.style.SUCCESS(url))
            datareader.next()
            ''' for row in datareader:

                data = Data(ticker = t, date = row[0], open_price = row[1], high_price = row[2], low_price = row[3], close_price = row[4], volume = int(row[5]), aclose_price = row[6])
                data.save()
                self.stdout.write(self.style.SUCCESS('Successfully entered line %s of data' % e))
                e += 1 '''
        self.stdout.write(self.style.SUCCESS('DONE!'))
