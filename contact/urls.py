# my_project/contact/urls.py

from django.urls import path
# from contact import views as contact_views # my_project/contact/contact_views.py
from contact.views import contact_views, contact_forms

# app_name = 'contact'
urlpatterns = [
     path('', contact_views.func_index, name='contact_index'), # my_project/contact/contact_views.py
     path('search/', contact_views.func_search, name='contact_search'), # my_project/contact/contact_views.py

     # Contact CRUD
     path('contacts/create/', contact_forms.func_create, name='contact_create'), # my_project/contact/contact_forms.py
     path('contacts/<int:contact_id>/read/', contact_views.func_contact, name='contact_contact'), # my_project/contact/contact_views.py
     path('contacts/<int:contact_id>/update/', contact_forms.func_update, name='contact_update'), # my_project/contact/contact_views.py
     path('contacts/<int:contact_id>/delete/', contact_forms.func_delete, name='contact_delete'), ## # my_project/contact/contact_views.py
]