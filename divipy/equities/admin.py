from divipy.equities.models import Portfolio
from django.contrib import admin
from .models import Etf, Stock, Portfolio
# Register your models here.
admin.site.register(Etf)
admin.site.register(Stock)
admin.site.register(Portfolio)