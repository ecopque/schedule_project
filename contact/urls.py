# my_project/contact/urls.py

from django.urls import path
from contact import views as contact_views # my_project/contact/views.py

# app_name = 'contact' #8:
urlpatterns = [
     path('', contact_views.func_index, name='contact_index') # my_project/contact/views.py
]