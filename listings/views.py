from django.shortcuts import render

def index(request):
    context= {
        
    }
    return render(request,'listings/listings.html',{'context':context})

def listing(request, listing_id):
    return render (request,'listings/listing.html')

def search(request):
    return render (request,'listings/search.html')