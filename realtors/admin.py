from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display=('id','name','phone','email','hire_date')
    list_display_links=('id','name',)
    search_fields=('name','phone')
    list_filter=("name",'phone','email')
    list_editable=("phone","email")
     

admin.site.register(Realtor,RealtorAdmin )


