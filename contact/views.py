from django.shortcuts import render

# Create your views here.

def func_index(request):
    return render(request, 'contact/index.html',) # my_project/contact/templates/contact/index.html