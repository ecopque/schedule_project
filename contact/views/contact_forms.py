# my_project/contact/views/contact_forms.py

from django.shortcuts import render
from contact.forms import cls_contactform # my_project/contact/forms.py

def func_create(request):
    # if request.method == 'POST':
    #     print(request.method)
    #     print(request.POST.get('first_name')) # my_project/contact/templates/contact/create.html
    #     print(request.POST.get('last_name')) # my_project/contact/templates/contact/create.html

    # POST method
    if request.method == 'POST':
        form = cls_contactform(data=request.POST) ##
        context = {'form':form} ## # my_project/contact/forms.py

        if form.is_valid(): ##
            print('Form is valid.')

        return render(request, 'contact/create.html', context) # my_project/contact/templates/contact/create.html
    
    # GET method
    context = {'form': cls_contactform()}
    return render(request, 'contact/create.html', context) # my_project/contact/templates/contact/create.html