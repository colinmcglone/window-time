from django.core.management.base import BaseCommand, CommandError
from marketgrab.models import Data, MovingAvg, Movements, Means
import datetime
import time

class Command(BaseCommand):
    help = 'Compute and store up to date means.'

    def add_arguments(self, parser):
        parser.add_argument('-t', '--tickers', nargs='+', required=True)

    def handle(self, **options):
        for e in options['tickers']:



            for i in [3, 5, 50, 200]:

