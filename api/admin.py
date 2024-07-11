from django.contrib import admin
from .models import Stake, UserBalance

# Register your models here.
admin.site.site_title = 'CoinToss Admin'
admin.site.site_header = 'CoinToss Admin'


admin.site.register(Stake)
admin.site.register(UserBalance)
