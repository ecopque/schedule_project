# my_project/contact/views/user_forms.py

from django.shortcuts import render
from contact.forms import cls_registerform ## # my_project/contact/forms.py

def func_register(request): ##
    form = cls_registerform() ##
    return render(request, 'contact/register.html', {'form': form}) ## # my_project/contact/templates/contact/register.html