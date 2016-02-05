from django.core.management.base import BaseCommand, CommandError
from marketgrab.models import Data, MovingAvg, Movements
import datetime, time

class Command(BaseCommand):
    help = 'Compute movements in market and moving averages'

    def add_arguments(self, parser):
        parser.add_argument('-t', '--tickers', nargs='+')
        parser.add_argument('-s', '--series', nargs='+')

    def handle(self, **options):
        for t in options['tickers']:
            if Data.objects.filter(ticker=t).exists():
                latest_data = Data.objects.filter(ticker=t).latest('date').date

                if Movements.objects.filter(ticker=t, series='market').exists():
                    latest_movement = Movements.objects.filter(ticker=t, series='market').latest('date').date
                else:
                    latest_movement = Data.objects.filter(ticker=t).earliest('date').date

                tt = datetime.datetime.now()
                if latest_movement < latest_data:
                    delta = Data.objects.filter(ticker=t, date__range=(latest_movement, latest_data)).count()
                    if delta == Data.objects.filter(ticker=t).count():
                        delta = delta - 1

                    ts = datetime.datetime.now()
                    tt = datetime.timedelta(seconds=0)

                    data = Data.objects.filter(ticker=t).order_by('-date')
                    length = len(data)
                    while delta > 0:
                        curr = data[delta-1:delta]
                        prev = data[delta:delta+1]
                        diff = curr[0].aclose_price - prev[0].aclose_price
                        percent = (diff/curr[0].aclose_price)*100

                        movement = Movements(ticker=t, date=curr[0].date, price=diff, percent_move=percent, series='market')
                        movement.save()

                        if not delta % 100:
                            tc = datetime.datetime.now()
                            tt = tc - ts
                            ts = datetime.datetime.now()
                            self.stdout.write(self.style.SUCCESS('%s %s %s' % (curr[0].date, t, tt.total_seconds())))
                        delta = delta - 1

                for s in options['series']:
                    if MovingAvg.objects.filter(span=s, ticker=t).exists:
                        latest_avg = MovingAvg.objects.filter(span=s, ticker=t).latest('date').date

                        if Movements.objects.filter(ticker=t, series=s).exists():
                            latest_movement = Movements.objects.filter(ticker=t, series=s).latest('date').date
                        else:
                            latest_movement = Data.objects.filter(ticker=t).earliest('date').date

                        if latest_movement < latest_avg:
                            delta = MovingAvg.objects.filter(span=s, ticker=t, date__range=(latest_movement, latest_data)).count()
                            if delta == MovingAvg.objects.filter(span=s, ticker=t).count():
                                delta = delta - 1

                            ts = datetime.datetime.now()
                            tt = datetime.timedelta(seconds=0)

                            data = MovingAvg.objects.filter(span=s, ticker=t).order_by('-date')
                            length = len(data)
                            while delta > 0:
                                curr = data[delta-1:delta]
                                prev = data[delta:delta+1]
                                diff = curr[0].price - prev[0].price
                                percent = (diff/curr[0].price)*100

                                movement = Movements(ticker=t, date=curr[0].date, price=diff, percent_move=percent, series=s)
                                movement.save()

                                if not delta % 100:
                                    tc = datetime.datetime.now()
                                    tt = tc - ts
                                    ts = datetime.datetime.now()
                                    self.stdout.write(self.style.SUCCESS('%s %s %s %s' % (curr[0].date, t, s, tt.total_seconds())))
                                delta = delta - 1
