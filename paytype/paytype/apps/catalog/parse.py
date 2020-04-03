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

# with io.open('COUNTY.csv', encoding='utf-8') as file:
#     reader = csv.DictReader(file, delimiter=',')
#     for line in reader:
#         print(line['CODE'])