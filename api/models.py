from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Stake(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    prediction = models.CharField(max_length=4, choices=(('HEAD', 'HEAD'), ('TAIL', 'TAIL')))
    result = models.CharField(max_length=4, choices=(('WIN', 'WIN'), ('LOSE', 'LOSE')), null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.user.username}'s stake of {self.amount} on {self.prediction} at {self.timestamp}"


class UserBalance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self) -> str:
        return self.balance
    