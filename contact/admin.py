# Register your models here.

#my_project/contact/admin.py

from django.contrib import admin
from contact.models import cls_contact # my_project/contact/models.py

@admin.register(cls_contact)
class cls_contactadmin(admin.ModelAdmin):
    ...