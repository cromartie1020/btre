from django.shortcuts import render
from .models import Listing
from realtors.models import Realtor

def index(request):
    listings=Listing.objects.all()
    realtors=Realtor.objects.all()
    context= {
        'listings':listings,
        'realtors':realtors
        
    }
    
    return render(request,'listings/listings.html',context)

def listing(request, id):
    listing=Listing.objects.get(id=id)
    listings=Listing.objects.all()
    realtor=listing.realtor
    name=listing.realtor.name
    print ('name:', name)
    context= {
        'listing':listing,
        'realtor':realtor,
        'listings':listings,
        'name':name,
        
    }
    return render (request,'listings/listing.html',context)

def search(request):
    return render (request,'listings/search.html')