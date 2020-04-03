from django.contrib import admin
from .models import PaymentsType, PaymentsCode, Country, PayType


admin.site.register(PaymentsType)
admin.site.register(PaymentsCode)
admin.site.register(Country)
admin.site.register(PayType)
