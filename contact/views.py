# my_project/contact/views.py

from django.shortcuts import render

def func_index(request):
    return render(request, 'contact/index.html',) # my_project/contact/templates/contact/index.html