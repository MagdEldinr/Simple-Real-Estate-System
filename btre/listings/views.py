from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import listing
from .choices import price_choices, bedrooms_choices, city_choices
# Create your views here.

def index(request):
    all_listings = listing.objects.all().order_by('-list_date').filter(is_published=True)
    paginator = Paginator(all_listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)

def one_listing(request, pk):
    data = listing.objects.get(pk=pk)
    context = {'listing': data}
    return render(request, 'listings/listing.html', context=context)

def search(request):
    search_result = listing.objects.order_by('-list_date').filter(is_published=True)

    #Keywords search
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            search_result = search_result.filter(description__icontains=keywords)

    #City Search
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            search_result = search_result.filter(city__iexact=city)

    #Bedrooms Search
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if city:
            search_result = search_result.filter(bedrooms__lte=bedrooms)
    
    #Price Search
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            search_result = search_result.filter(price__lte=price)



    paginator = Paginator(search_result, 2)
    page = request.GET.get('page')
    paged__result_listings = paginator.get_page(page)
    context = {
        'bedrooms_choices': bedrooms_choices,
        'price_choices': price_choices,
        'city_choices': city_choices,
        'listings': paged__result_listings,
        'search_values': request.GET
        }
    return render(request, 'listings/search.html', context=context)