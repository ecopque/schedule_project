# my_project/contact/views/contact_views.py

from django.shortcuts import render
from contact.models import cls_contact # my_project/contact/models.py

def func_index(request):
    # contacts = cls_contact.objects.all().order_by('-id')
    contacts = cls_contact.objects.filter(show=True).order_by('-id') ##
    context = {'contacts': contacts,}

    return render(request, 'contact/index.html', context) # my_project/contact/templates/contact/index.html