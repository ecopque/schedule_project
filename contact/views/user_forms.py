# my_project/contact/views/user_forms.py

from django.shortcuts import render
from contact.forms import cls_registerform # my_project/contact/forms.py
from django.contrib import messages
from django.shortcuts import redirect

def func_register(request): #% my_project/contact/urls.py
    form = cls_registerform()
    
    messages.info(request, 'Any text.')
    messages.success(request, 'Any text.')
    messages.warning(request, 'Any text.')
    messages.error(request, 'Any text.')

    if request.method == 'POST':
        form = cls_registerform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registered user.')
            return redirect('contact_index')
    return render(request, 'contact/register.html', {'form': form}) # my_project/contact/templates/contact/register.html