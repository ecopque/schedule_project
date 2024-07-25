# my_project/contact/urls.py

from django.urls import path
from contact import views as contact_views # my_project/contact/contact_views.py

# app_name = 'contact'
urlpatterns = [
     path('', contact_views.func_index, name='contact_index'), # my_project/contact/contact_views.py
     path('<int:contact_id>/', contact_views.func_contact, name='contact_contact') ##  ##AAA # my_project/contact/contact_views.py
]