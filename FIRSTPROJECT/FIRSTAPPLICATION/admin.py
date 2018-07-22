from django.contrib import admin

# Register your models here.
from FIRSTAPPLICATION.models import Name_ID, Contact, Address

admin.site.register(Name_ID)
admin.site.register(Contact)
admin.site.register(Address)