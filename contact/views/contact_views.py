# my_project/contact/views/contact_views.py

from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from contact.models import cls_contact # my_project/contact/models.py
from django.http import Http404
from django.core.paginator import Paginator

def func_index(request):
    # contacts = cls_contact.objects.all().order_by('-id')
    contacts = cls_contact.objects.filter(show=True).order_by('-id')
    print(contacts.query)
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    # context = {'contacts': contacts, 'site_title': 'Contacts - '}
    context = {'page_obj': page_obj, 'site_title': 'Contacts - '} # my_project/contact/templates/contact/index.html

    return render(request, 'contact/index.html', context) # my_project/contact/templates/contact/index.html

def func_contact(request, contact_id):
    single_contact = cls_contact.objects.filter(pk=contact_id, show=True).first()
    if single_contact is None:
        raise Http404()
    contact_name = f'{single_contact.first_name} {single_contact.last_name} -' # my_project/contact/models.py
    context = {'contact': single_contact, 'site_title': contact_name} # my_project/contact/templates/contact/contact.html

    return render(request, 'contact/contact.html', context)

def func_search(request):
    search_value = request.GET.get('q', '').strip() # my_project/base_templates/partials/_header.html
    print('search_value: ', search_value)
    if search_value == '':
        return redirect('contact_index') # my_project/contact/urls.py
    contacts = cls_contact.objects.filter(show=True).filter(Q(first_name__icontains=search_value) | Q(last_name__icontains=search_value) |  Q(phone__icontains=search_value) |  Q(email__icontains=search_value)).order_by('-id') # my_project/contact/models.py

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'site_title': 'Search - '}

    # context = {'contacts': contacts, 'site_title': 'Search - '}
    return render(request, 'contact/index.html', context)