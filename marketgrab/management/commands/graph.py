from django.core.management.base import BaseCommand, CommandError
from marketgrab.models import Data, MovingAvg, Movements
from django.db.models import Avg, Min, Max
import datetime
import time
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np

class Command(BaseCommand):
    help = 'Compute and store up to date moving averages'

    def add_arguments(self, parser):
        parser.add_argument('-t', '--tickers', nargs='+', required=True)

    def handle(self, **options):
        for t in options['tickers']:
            '''data = Data.objects.filter(ticker=t).order_by('date')
            x = np.array([i.date for i in data])
            y = np.array([i.aclose_price for i in data])
            plt.plot(x, y)
            plt.savefig(t + '_data.png')
            plt.close()'''
            
            move = Movements.objects.filter(ticker=t, series='market')
            count = move.count()
            x = np.array([i.percent_move for i in move])
            mu = Movements.objects.filter(ticker=t, series='market').aggregate(mean=Avg('percent_move'))['mean']
            min = Movements.objects.filter(ticker=t, series='market').aggregate(min=Min('percent_move'))['min']
            max = Movements.objects.filter(ticker=t, series='market').aggregate(max=Max('percent_move'))['max']
            sigma = np.std(np.array([i.percent_move for i in move]))
            b = [min]
            b.extend(np.arange(-5, 5, 0.1))
            b.extend([max])
            
            n, bins, patches = plt.hist(x, b, normed=1, facecolor='blue', alpha=0.75)
            
            y = mlab.normpdf( bins, mu, sigma)
            l = plt.plot(bins, y, 'r--', linewidth=1)
            
            plt.xlabel('Price Movement')
            plt.ylabel('Frequency')
            plt.axis([-5.5, 5.5, 0, .7])
            plt.title('Histogram of Daily Movements in %s \n Max: %s, Min: %s, Mean: %s, Standard Deviation:%s' % (t, round(max, 1), round(min, 1), round(mu, 4), round(sigma, 4)))
            plt.grid(True)
            
            plt.savefig(t + '_hist.png')
            plt.close()

            '''for s in [3, 5, 50, 200]:
                avg = MovingAvg.objects.filter(ticker=t, span=s).order_by('date')
                x = np.array([i.date for i in avg])
                y = np.array([i.price for i in avg])
                plt.plot(x, y)
                plt.savefig(t + '_' + str(s) + '_movingavg.png')
                plt.close()
            '''