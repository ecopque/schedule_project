# my_project/contact/views/contact_views.py

from django.shortcuts import render
from contact.models import cls_contact # my_project/contact/models.py

def func_index(request):
    # contacts = cls_contact.objects.all().order_by('-id')
    contacts = cls_contact.objects.filter(show=True).order_by('-id')
    print(contacts.query)
    context = {'contacts': contacts,}

    return render(request, 'contact/index.html', context) # my_project/contact/templates/contact/index.html

def func_contact(request, contact_id): ##
    single_contact = cls_contact.objects.get(pk=contact_id) ##
    context = {'contact': single_contact,} ## # my_project/contact/templates/contact/contact.html

    return render(request, 'contact/contact.html', context) ##