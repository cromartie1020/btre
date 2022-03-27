from django.shortcuts import render, redirect
from .models import Listing
from realtors.models import Realtor
from .choices import *
from .forms import Inquiry_form
from .models import Inquiry

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
    listings=Listing.objects.all()
    queryset_list=Listing.objects.all()
    
    
    realtors=Realtor.objects.all()
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            queryset_list=queryset_list.filter(description__icontains=keywords)
            
    for query in queryset_list:
        print('query',queryset_list )          
    
    context={
        'realtors':realtors,
        'price_choices':price_choices,
        'bedroom_choices':bedroom_choices,
        'state_choices':state_choices,
        'listings':queryset_list,     
        
    }
    for query in queryset_list:
        print ('query',queryset_list)
    
    
    return render(request,'listings/search.html',context)
    

def listings_all(request):
    
    
    listings=Listing.objects.all().filter(is_published=True)
    
    realtors=Realtor.objects.all()
    context={
        'listings':listings,
        'realtors':realtors,
        'price_choices':price_choices,
        'bedroom_choices':bedroom_choices,
        'state_choices':state_choices,
        
        
    }
    
    
    return render(request, 'listings/listings_all.html',context)

def inquiry_view(request):
    form = Inquiry_form(request.POST or None)
   
        
    if form.is_valid():
        form.save()
              
    
    return render(request, 'listings/inquiry.html',{'form':'form'})
        
            