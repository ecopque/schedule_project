# Register your models here.

# my_project/contact/admin.py

from django.contrib import admin
from contact.models import cls_contact # my_project/contact/models.py

@admin.register(cls_contact)
class cls_contactadmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone',) # my_project/contact/models.py
    ordering = ('-id',) #AAA:
    list_filter = ('created_date',) # my_project/contact/models.py