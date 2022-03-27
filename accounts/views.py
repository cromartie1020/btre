from django.shortcuts import render,redirect
from django.contrib import messages, auth  
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as logout_view
from realtors.models import Realtor
from listings.models import Listing
from listings import choices


def login(request):
    
    if request.method == 'POST':
    
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request,user)
            messages.success(request, "you are now logged in.")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('login')
            
    
    return render(request,'accounts/login.html')
    
    


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # Check if passwords match 
        if password==password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request,'User name is already taken.')
                
                return redirect('index')
                
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email is already taken.')
                    return redirect('register')
                else:
                    # Looks good 
                    user=User.objects.create_user(first_name=first_name,username=username,last_name=last_name,email=email,password=password)
                    # login after register
                    
                    user.save()
                    messages.success(request, 'You are now registered and can now  logged in')
                    return redirect('index') 
                    
                                  
                
                
        else:
            messages.error(request,'Passwords do not match.')
            return redirect('register') 
        
           
        
    else:
    
        return render(request,'accounts/register.html')
    
def logout(request):
    logout_view(request)
    
    return redirect('index')
    

def dashboard(request):
    
    print(user.username)
    listings=Listing.objects.all().filter(is_published=True   )
    
    realtors=Realtor.objects.all()
    context={
        'listings':listings,
        'realtors':realtors,
        
        
        
    }
    
    return render(request,'accounts/dashboard.html', context)

    