import django
from django.db import models


class PaymentType(models.TextChoices):
    MONEY = 'Rial'
    AD = 'Ad'


class Currency(models.TextChoices):
    DOLLAR = 'Dollar'
    LIRA = 'Lira'
    RIAL = 'Rial'


class RewardType(models.TextChoices):
    COIN = 'Coin',
    GEM = 'Gem'
    CARD = 'Card'


class StoreItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    reward = models.IntegerField(default=0)
    rewardType = models.CharField(max_length=10, choices=RewardType.choices, default=RewardType.COIN)
    price = models.IntegerField(default=0)
    paymentType = models.CharField(max_length=10, choices=PaymentType.choices, default=PaymentType.MONEY)
    currency = models.CharField(max_length=10, choices=Currency.choices, default=Currency.DOLLAR)

    createDate = models.DateTimeField(default=django.utils.timezone.now)

    def get(self):
        return {'name': self.name,
                'description': self.description,
                'reward': self.reward,
                'rewardType': self.rewardType,
                'price': self.price,
                'paymentType': self.paymentType,
                'currency': self.currency}

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    reward = models.IntegerField(default=0)
    rewardType = models.CharField(max_length=10, choices=RewardType.choices, default=RewardType.COIN)
    price = models.IntegerField(default=0)
    paymentType = models.CharField(max_length=10, choices=PaymentType.choices, default=PaymentType.MONEY)
    currency = models.CharField(max_length=10, choices=Currency.choices, default=Currency.DOLLAR)

    createDate = models.DateTimeField(default=django.utils.timezone.now)

    def get(self):
        return {'name': self.name,
                'description': self.description,
                'reward': self.reward,
                'rewardType': self.rewardType,
                'price': self.price,
                'paymentType': self.paymentType,
                'currency': self.currency}

    def __str__(self):
        return self.name
