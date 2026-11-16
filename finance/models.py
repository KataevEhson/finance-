from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User





class Wallet(models.Model):
    balance = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateField(default=datetime.now)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.balance


class History_tranzaction(models.Model):
    wallet_id = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount = models.CharField()
    type_tranzaction = models.CharField()
    info = models.CharField()
    def __str__(self):
        return self.amount