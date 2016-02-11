from django.core.management.base import BaseCommand, CommandError
from marketgrab.models import Data, MovingAvg, Movements, Sigma
import numpy as np
from datetime import date
from django.db.models import Avg

class Command(BaseCommand):
    help = 'Compute and store up to date sigma for movements.'

    def add_arguments(self, parser):
        parser.add_argument('-t', '--tickers', nargs='+', required=True)

    def handle(self, **options):
        for t in options['tickers']:
            try:
                latest_s = Sigma.objects.filter(ticker=t, series='market').latest('date').date
            except:
                latest_s = date.min

            latest_m = Movements.objects.filter(ticker=t, series='market').latest('date').date
            if latest_s < latest_m:
                move = Movements.objects.filter(ticker=t, series='market')
                sigma = np.std(np.array([i.percent for i in move]))
                d = move.latest('date').date
                s = Sigma(ticker=t, date=d, value=sigma, series='market')
                s.save()

                for s in [3, 5, 50, 200]:
                    move = Movements.objects.filter(ticker=t, series=s)
                    sigma = np.std(np.array([i.percent for i in move]))
                    d = move.latest('date').date
                    s = Sigma(ticker=t, date=d, value=sigma, series=s)
                    s.save()
