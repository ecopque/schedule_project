# my_project/contact/views/contact_forms.py

from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from contact.models import cls_contact # my_project/contact/models.py
from django.http import Http404
from django.core.paginator import Paginator

def func_create(request):
    context = {}
    return render(request, 'contact/create.html', context) ##