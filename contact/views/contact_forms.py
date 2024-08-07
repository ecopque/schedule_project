# my_project/contact/views/contact_forms.py

from django.shortcuts import render
from contact.forms import cls_contactform # my_project/contact/forms.py
from django.shortcuts import redirect
from django.urls import reverse ##

def func_create(request):
    # if request.method == 'POST':
    #     print(request.method)
    #     print(request.POST.get('first_name')) # my_project/contact/templates/contact/create.html
    #     print(request.POST.get('last_name')) # my_project/contact/templates/contact/create.html

    # POST method
    form_action = reverse('contact_create') ##
    if request.method == 'POST':
        form = cls_contactform(data=request.POST)
        context = {'form':form, 'form_action': form_action} ##

        if form.is_valid():
            contact = form.save(commit=False)
            contact.show = False
            contact.save()
            return redirect('contact_update', contact_id=contact.pk) ## # my_project/contact/urls.py

        return render(request, 'contact/create.html', context) # my_project/contact/templates/contact/create.html

    # GET method
    # context = {'form': cls_contactform()}
    context = {'form':form, 'form_action': form_action} ##
    return render(request, 'contact/create.html', context) # my_project/contact/templates/contact/create.html