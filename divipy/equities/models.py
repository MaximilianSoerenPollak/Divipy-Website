from django.db import models
from django.db.models.deletion import CASCADE
from shortuuidfield import ShortUUIDField
from users.models import User
from django.utils import timezone

# Create your models here.
class BaseEquity(models.Model):
    long_name = models.CharField(max_length=256, verbose_name="Stock Name", default="NaN", blank=True)
    symbol = models.CharField(max_length=32, unique=True, verbose_name="Ticker", default="NaN", blank=True)
    sector = models.CharField(max_length=64, default="NaN", blank=True)
    industry = models.CharField(max_length=64, default="NaN", blank=True)
    website = models.CharField(max_length=256, default="NaN", blank=True)
    long_business_summary = models.TextField(verbose_name="Business Description", default="NaN", blank=True)
    current_price = models.FloatField(verbose_name="Price", default="NaN", blank=True)
    one_year_low = models.FloatField(default="NaN", blank=True)
    one_year_high = models.FloatField(default="NaN", blank=True)
    dividend_rate = models.FloatField(default="NaN", blank=True)
    dividend_yield = models.FloatField(default="NaN", blank=True)
    five_year_avg_div_yield = models.FloatField(default="NaN", blank=True)
    payout_months = models.PositiveSmallIntegerField(default="NaN", blank=True)
    payout_ratio = models.FloatField(default="NaN", blank=True)
    market_cap = models.FloatField(default="NaN", blank=True)
    profit_margin = models.PositiveBigIntegerField(default="NaN", blank=True)
    beta = models.FloatField(default="NaN", blank=True)
    reccomendation = models.CharField(max_length=256, default="NaN", blank=True)
    date_updated = models.DateField(default=timezone.now, blank=True)
    user_created = models.BooleanField(default=False)
    
    class Meta:
        abstract = True
    
    def __str__(self) -> str:
        return self.long_name

class Portfolio(models.Model):
    uuid = ShortUUIDField(max_length=6, primary_key=True)
    title = models.CharField(max_length=256)
    active = models.BooleanField()
    user = models.ForeignKey(User, on_delete=CASCADE)
    
    def __str__(self) -> str:
        return self.title 


class Etf(BaseEquity):
    
    etf = models.ForeignKey(Portfolio, related_name="etf")


class Stock(BaseEquity):

    stock = models.ForeignKey(Portfolio, related_name="stock")