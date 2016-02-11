from marketgrab.models import Data, MovingAvg, Movements, Sigma
import numpy as np
from django.db.models import Avg

class Command(BaseCommand):
    help = 'Compute and store up to date sigma for movements.'

    def add_arguments(self, parser):
        parser.add_argument('-t', '--tickers', nargs='+', required=True)

    def handle(self, **options):
        for t in options['tickers']:
            move = Movements.objects.filter(ticker=t, series='market')
            sigma = np.std(np.array([i.percent for i in move]))
            d = move.latest('date').date
            s = Sigma(ticker=t, date=d, value=sigma, series='market')
            s.save()

                        n = MovingAvg(ticker=e, date=avg_set[0].date, price=x, span=i)
