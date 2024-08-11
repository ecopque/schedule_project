# my_project/contact/views/user_forms.py

from django.shortcuts import render

def func_register(request):
    return render(request, 'contact/register.html')