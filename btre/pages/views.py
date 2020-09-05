from django.shortcuts import render
from django.http import HttpResponse

from listings.models import listing
from realtors.models import Realtor
from listings.choices import bedrooms_choices, price_choices, city_choices

# Create your views here.

def index(request):
    last_listings = listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': last_listings,
        'bedrooms_choices': bedrooms_choices,
        'price_choices': price_choices,
        'city_choices': city_choices
        }
    return render(request, template_name='pages/index.html', context=context)

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')

    #Get seller of the month
    mvp = Realtor.objects.filter(is_mvp=True)[0]
    context = {
        'realtors': realtors,
        'mvp': mvp
    }
    return render(request, template_name='pages/about.html', context=context)  