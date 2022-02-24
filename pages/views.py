from django.shortcuts import render
from django.http import HttpResponse
from realtors.models import Realtor
from listings.models import Listing
from listings.choices import price_choices, bedroom_choices, state_choices

def index(request):
    listings=Listing.objects.all()[0:3]
    realtors=Realtor.objects.all()
    context={
        'listings':listings,
        'realtors':realtors,
        'price_choices':price_choices,
        'bedroom_choices':bedroom_choices,
        'state_choices':state_choices,
        
        
    }
    
    
    return render(request, 'pages/index.html',context)


def about(request):
    return render(request, 'pages/about.html')



