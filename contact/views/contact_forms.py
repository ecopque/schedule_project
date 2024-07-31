# my_project/contact/views/contact_forms.py

from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from contact.models import cls_contact # my_project/contact/models.py
from django.http import Http404
from django.core.paginator import Paginator
from django import forms ##

class cls_contactform(forms.ModelForm): ##
    class Meta: ##
        model = cls_contact ##
        fields = ('first_name', 'last_name', 'phone',) ##

def func_create(request):
    # if request.method == 'POST':
    #     print(request.method)
    #     print(request.POST.get('first_name')) # my_project/contact/templates/contact/create.html
    #     print(request.POST.get('last_name')) # my_project/contact/templates/contact/create.html


    context = {}
    return render(request, 'contact/create.html', context) # my_project/contact/templates/contact/create.html