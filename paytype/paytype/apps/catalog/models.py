from django.db import models


class PaymentsType(models.Model):
    payment_type = models.IntegerField()


class PaymentsCode(models.Model):
    payment_code = models.IntegerField()


class Country(models.Model):
    code = models.IntegerField()


class PayType(models.Model):
    description = models.TextField(blank=True)
    p_type = models.ForeignKey(PaymentsType, on_delete=models.CASCADE)
    route = models.CharField(max_length=10, blank=True)
    p_code = models.ForeignKey(PaymentsCode, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, related_name='country', null=True)
    countries = models.ManyToManyField(Country, related_name='countries', blank=True, null=True)
    not_country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, related_name='not_country', null=True)
    not_countries = models.ManyToManyField(Country, related_name='not_countries', blank=True, null=True)
    feature = models.IntegerField(blank=True, null=True)
    start_date = models.DateField()
    finish_date = models.DateField()
    document = models.CharField(max_length=50, blank=True)
