from django.contrib import admin
from .models import Quote, FiveDay, FiftyDay, TwoHundredDay
# Register your models here.

admin.site.register(Quote)
admin.site.register(FiveDay)
admin.site.register(FiftyDay)
admin.site.register(TwoHundredDay)
