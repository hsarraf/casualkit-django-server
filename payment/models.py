import django
from django.db import models
from store.models import StoreItem


class Receipt(StoreItem):
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Payment(models.Model):
    userId = models.UUIDField(primary_key=True, editable=False)
    username = models.CharField(max_length=50, unique=True)

    receipts = models.ManyToManyField(Receipt, blank=True, related_name='payment_receipts')

    pricePaid = models.IntegerField(default=0)
    adWatched = models.IntegerField(default=0)

    createDate = models.DateTimeField(default=django.utils.timezone.now)
    log = models.TextField(default='', blank=True)

    def get_receipts(self):
        return [receipt.get() for receipt in self.receipts.all()]

    def __str__(self):
        return self.username
