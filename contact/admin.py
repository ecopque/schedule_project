# Register your models here.

# my_project/contact/admin.py

from django.contrib import admin
from contact.models import cls_contact # my_project/contact/models.py

@admin.register(cls_contact)
class cls_contactadmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone',) # my_project/contact/models.py
    ordering = ('-id',)
    list_filter = ('created_date',) # my_project/contact/models.py
    search_fields = ('id', 'first_name', 'last_name',) # my_project/contact/models.py
    list_per_page = 50
    list_max_show_all = 1000
    # list_editable = ('first_name', 'last_name',) # my_project/contact/models.py
    list_display_links = ('id', 'phone',) # my_project/contact/models.py