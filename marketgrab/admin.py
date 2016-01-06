from django.contrib import admin
from .models import Data, FiveDay, FiftyDay, TwoHundredDay
# Register your models here.

admin.site.register(Data)
admin.site.register(FiveDay)
admin.site.register(FiftyDay)
admin.site.register(TwoHundredDay)
