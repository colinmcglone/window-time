from django.core.management.base import BaseCommand, CommandError
from marketgrab.models import Data, MovingAvg
import datetime
import time

class Command(BaseCommand):
    help = 'Compute and store up to date moving averages'

    def add_arguments(self, parser):
        parser.add_argument('-t', '--tickers', nargs='+', required=True)
        parser.add_argument('-s', '--spans', nargs='+', required=True)

    def handle(self, **options):
        for e in options['tickers']:
            latest_data = Data.objects.filter(ticker=e).latest('date')
            latest_data = latest_data.date
            first_data = Data.objects.filter(ticker=e).earliest('date')
            first_data = first_data.date
            for i in options['spans']:
                i = int(i)
                try:
                    latest_average = MovingAvg.objects.filter(ticker=e, span=i).latest('date')
                    latest_average = latest_average.date

                except MovingAvg.DoesNotExist:
                    latest_average = first_data

                if latest_average < latest_data:
                    delta = Data.objects.filter(ticker=e, date__range=(latest_average, latest_data)).count()
                    ts = datetime.datetime.now()
                    tt = datetime.timedelta(seconds=0)

                    while i < delta:
                        oldest = delta
                        newest = delta - i
                        avg_set = Data.objects.filter(ticker=e).order_by('-date')[newest:oldest]
                        x = 0
                        if len(avg_set) == i:
                            for each in avg_set:
                                x = x + each.aclose_price
                            x = x/i
                        n = MovingAvg(ticker=e, date=avg_set[0].date, price=x, span=i)
                        n.save()
                        delta = delta - 1

                        td = datetime.datetime.now() - ts
                        tt = tt + td
                        ts = datetime.datetime.now()

                        if not delta % 100:
                            self.stdout.write(self.style.SUCCESS('%s %s day average for %s updated! %s' % (e, i, avg_set[0].date, tt.total_seconds())))
                            tt = datetime.timedelta(seconds=0)
                else:
                    self.stdout.write(self.style.SUCCESS('No averages to update.'))
