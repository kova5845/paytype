from catalog.models import PaymentsType, PaymentsCode, Country, PayType
import csv
import io


with io.open('COUNTY.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=',')
    for line in reader:
        try:
            go = Country.objects.get(code=int(line['CODE']))
        except Country.DoesNotExist:
            go = None
        if go == None:
            p = Country(code=int(line['CODE']))
            p.save()

with io.open('PAYMENSTYPE.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=',')
    for line in reader:
        try:
            go = PaymentsType.objects.get(payment_type=int(line['PAYMENTTYPE']))
        except PaymentsType.DoesNotExist:
            go = None
        if go == None:
            p = PaymentsType(payment_type=int(line['PAYMENTTYPE']))
            p.save()

with io.open('PAYMENSTYPE.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=',')
    for line in reader:
        try:
            go = PaymentsCode.objects.get(payment_code=int(line['PAYMENTCODE']))
        except PaymentsCode.DoesNotExist:
            go = None
        if go == None:
            p = PaymentsCode(payment_code=int(line['PAYMENTCODE']))
            p.save()
