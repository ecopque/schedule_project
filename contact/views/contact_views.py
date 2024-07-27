# my_project/contact/views/contact_views.py

from django.shortcuts import render
from contact.models import cls_contact # my_project/contact/models.py
from django.http import Http404

def func_index(request):
    # contacts = cls_contact.objects.all().order_by('-id')
    contacts = cls_contact.objects.filter(show=True).order_by('-id')
    print(contacts.query)
    context = {'contacts': contacts, 'site_title': 'Contacts - '}

    return render(request, 'contact/index.html', context) # my_project/contact/templates/contact/index.html

def func_contact(request, contact_id):
    single_contact = cls_contact.objects.filter(pk=contact_id, show=True).first()
    if single_contact is None:
        raise Http404()
    contact_name = f'{single_contact.first_name} {single_contact.last_name} -' # my_project/contact/models.py
    context = {'contact': single_contact, 'site_title': contact_name} # my_project/contact/templates/contact/contact.html

    return render(request, 'contact/contact.html', context)