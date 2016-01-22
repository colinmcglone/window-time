from django.core.management.base import BaseCommand, CommandError
from marketgrab.models import Data, MovingAvg
import datetime
import time
import matplotlib.pyplot as plt
import numpy as np

class Command(BaseCommand):
    help = 'Compute and store up to date moving averages'

    def add_arguments(self, parser):
        parser.add_argument('-t', '--tickers', nargs='+', required=True)

    def handle(self, **options):
        for t in options['tickers']:
            data = Data.objects.filter(ticker=t).order_by('date')
            x = np.array([i.date for i in data])
            y = np.array([i.aclose_price for i in data])
            plt.plot(x, y)
            plt.savefig(t + '_data.png')
            plt.close()

            for s in [3, 5, 50, 200]:
                avg = MovingAvg.objects.filter(ticker=t, span=s).order_by('date')
                x = np.array([i.date for i in avg])
                y = np.array([i.price for i in avg])
                plt.plot(x, y)
                plt.savefig(t + '_' + str(s) + '_movingavg.png')
                plt.close()
