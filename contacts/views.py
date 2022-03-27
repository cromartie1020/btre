from django.shortcuts import render, redirect
from listings.models import Listing
from django.contrib import messages
from . models import Contact
from django.core.mail import send_mail

def contact(request):
    
    if request.method == 'POST':
        listing_id=request.POST['listing_id']
        listing=request.POST['listing']
        name=request.POST['name']
        phone=request.POST['phone']
        email = request.POST['email']
        user_id=request.POST['user_id']
        message=request.POST['message']
        realtor_email=request.POST['realtor_email']
        
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted =Contact.objects.all().filter(listing_id=listing_id, user_id = user_id )
            if has_contacted:
                messages.error(request, "You have already made an inquiry for this listing.")
                return redirect('/listing/' + listing_id)               
        
        contact=Contact(listing = listing, listing_id = listing_id, name = name, email = email, phone = phone, message = message, user_id = user_id )
        
        contact.save()
        
        '''    
        send_mail(
            'Subject here',
            'Here is the message.',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )
        '''    
        send_mail(
            'Propert Listing Inquiry',
            'There has been an inquiry for ' + ' . Sign into the admin panel for more info.',
            'hrc245@gmail.com',
            [realtor_email,'hrc345@gmail.com'],
            
            fail_silently=False  
                      
        )
        
        messages.success(request, 'Your request has been submitted a realtor will get back to you soon.')
        return redirect('/listing/' + listing_id)
        
        
        
   