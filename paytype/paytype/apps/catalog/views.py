from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import PaymentsType, PaymentsCode, Country, PayType
from django.urls import reverse
from datetime import datetime


def index(request):
    return HttpResponse('Hello World!')


def paytype_view(request):
    my_list = PayType.objects.all()
    paginator = Paginator(my_list, 5)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'paytype_view.html', {'contacts': contacts})


def paytype_view_id(request, paytype_id):
    paytype = PayType.objects.get(id=paytype_id)
    return render(request, 'paytype_view_id.html', {'paytype': paytype})


def paytype_add(request):
    p_type = PaymentsType.objects.all()
    p_code = PaymentsCode.objects.all()
    country = Country.objects.all()
    return render(request, 'paytype_add.html', {
        'p_type': p_type,
        'p_code': p_code,
        'country': country
    })


def paytype_add_add(request):
    paytype = PayType()
    paytype.description = request.POST['description']
    paytype.start_date = datetime.strptime(request.POST['start_date'], '%Y-%m-%d').date()
    paytype.finish_date = datetime.strptime(request.POST['finish_date'], '%Y-%m-%d').date()
    if request.POST['feature'] == '':
        feature = None
    else:
        feature = int(request.POST['country'])
    paytype.feature = feature
    paytype.document = request.POST['document']
    paytype.route = request.POST['route']
    p_type = PaymentsType.objects.get(payment_type=int(request.POST['p_type']))
    paytype.p_type = p_type
    p_code = PaymentsCode.objects.get(payment_code=int(request.POST['p_code']))
    paytype.p_code = p_code
    paytype.save()
    if request.POST['country'] == '':
        country = None
    else:
        country = Country.objects.get(code=int(request.POST['country']))
    paytype.country = country
    if request.POST['not_country'] == '':
        not_country = None
    else:
        not_country = Country.objects.get(code=int(request.POST['not_country']))
    paytype.not_country = not_country
    if paytype.country == paytype.not_country:
        paytype.not_country = None
    # countries = []
    for cn in request.POST.getlist('countries'):
        paytype.countries.add(Country.objects.get(code=cn))
    for cn in request.POST.getlist('not_countries'):
        paytype.not_countries.add(Country.objects.get(code=cn))
    # not_countries = []
    # for cn in request.POST.getlist('not_countries'):
    #     not_countries.append(Country.objects.get(code=cn))
    # for c in countries:
    #     if c in not_countries:
    #         not_countries.remove(c)
    # print(not_countries)
    # print(countries)
    # paytype.not_countries.set(request.POST.getlist('not_countries'))
    # paytype.countries.set(request.POST.getlist('countries'))

    paytype.save()
    return HttpResponseRedirect(reverse('catalog:paytype_view'))
