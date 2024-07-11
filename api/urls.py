from django.urls import path
from .views import StakeCreateView, StakeHistoryView

app_name = 'api'

urlpatterns = [
    path('stake/create/', StakeCreateView.as_view(), name='stake-create'),
    path('stake/history/', StakeHistoryView.as_view(), name='stake-history'),
]
