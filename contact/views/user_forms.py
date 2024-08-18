# my_project/contact/views/user_forms.py
# Create user: http://127.0.0.1:8000/user/create/
# Login user: http://127.0.0.1:8000/user/login/

from django.shortcuts import render
from contact.forms import cls_registerform # my_project/contact/forms.py
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from contact.forms import cls_registerupdateform
from django.contrib.auth.decorators import login_required ##

def func_register(request): #% my_project/contact/urls.py
    form = cls_registerform()
    messages.info(request, 'Any text.')
    # messages.success(request, 'Any text.')
    # messages.warning(request, 'Any text.')
    # messages.error(request, 'Any text.')
    if request.method == 'POST':
        form = cls_registerform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registered user.')
            return redirect('contact_login') # my_project/contact/urls.py
    return render(request, 'contact/register.html', {'form': form}) # my_project/contact/templates/contact/register.html

@login_required(login_url='contact_login') ##A: # my_project/contact/urls.py
def func_userupdate(request):
    form = cls_registerupdateform(instance=request.user)
    if request.method != 'POST':
        return render(request, 'contact/user_update.html', {'form': form})
    form = cls_registerupdateform(data=request.POST, instance=request.user)
    if not form.is_valid():
        return render(request, 'contact/user_update.html', {'form': form})
    else:
        form.save()
        return redirect('contact_user_update')

def func_loginview(request):
    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Login made successfully.')
            print('Authenticated user (not logged):', user)
            return redirect('contact_index') # my_project/contact/urls.py
        else:
            messages.error(request, 'Invalid login.')
    return render(request, 'contact/login.html', {'form': form}) # my_project/contact/templates/contact/login.html

@login_required(login_url='contact_login') ##A: # my_project/contact/urls.py
def func_logoutview(request):
    auth.logout(request)
    return redirect('contact_login')