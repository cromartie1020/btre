from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('listing/',views.listings_all,name='listings_all'),
    path('<int:id>/',views.listing, name='listing'),
    path('inquiry/',views.inquiry_view, name='inquiry')
   
]
