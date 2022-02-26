from django.shortcuts import render
from django.http import HttpResponse
from realtors.models import Realtor
from listings.models import Listing
from listings.choices import price_choices, bedroom_choices, state_choices

def index(request):
    
    listings=Listing.objects.all().filter(is_published=True)[0:3]
    
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



def search(request):
    
   
    queryset_list=Listing.objects.all()
    city=Listing.objects.all()
    realtors=Realtor.objects.all()
    
    
    # keywords
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            queryset_list=queryset_list.filter(description__icontains=keywords)
            print ('This is my queryset_list',queryset_list)
    
    # city
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            queryset_list=queryset_list.filter(city__icontains=city)
            
    
    if 'state' in request.GET:
        states=request.GET['state']
        if state:
            queryset_list=queryset_list.filter(state__exact=states)
            
    if 'bedrooms' in request.GET:
        bedrooms=request.GET['bedrooms']
        if bedrooms:
            queryset_list=queryset_list.filter(bedrooms__exact=bedrooms)
            
    if 'zip' in request.GET:
        zip=request.GET['zip']
        if zip:
            queryset_list=queryset_list.filter(zip__contains=zip)
            
    if 'price' in request.GET:
        price=request.GET['price']
        if price == '$1M+':
            price=1000000
        else:
            
             
            #lets remove the $
            
            price=price[1:]              # Remove the first character the $ 
            if ',' in price:
                price=price.replace(',','')  # Remove the comma.
                price=int(price)             # Change to an integer.
        
            
        if price:
            queryset_list=queryset_list.filter(price__lte=price)
                    
            
    print(queryset_list)     
    context= {
        'realtors':realtors,
        'price_choices':price_choices,
        'bedroom_choices':bedroom_choices,
        'state_choices':state_choices,
        'listings':queryset_list,     
        
    }
    
    return render(request,'listings/search.html',context)