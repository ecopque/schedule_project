# my_project/contact/views/contact_forms.py

from django.shortcuts import render
from contact.forms import cls_contactform # my_project/contact/forms.py

# Moved to forms.py
# class cls_contactform(forms.ModelForm):
#     class Meta:
#         model = cls_contact
#         fields = ('first_name', 'last_name', 'phone',) # (# my_project/contact/templates/contact/create.html)

#     def clean(self):
#         cleaned_data = self.cleaned_data
#         self.add_error('first_name', ValidationError('Error message.', code='invalid'))
#         return super().clean()

def func_create(request):
    # if request.method == 'POST':
    #     print(request.method)
    #     print(request.POST.get('first_name')) # my_project/contact/templates/contact/create.html
    #     print(request.POST.get('last_name')) # my_project/contact/templates/contact/create.html

    # POST method
    if request.method == 'POST':
        context = {'form': cls_contactform(data=request.POST)}
        return render(request, 'contact/create.html', context) # my_project/contact/templates/contact/create.html
    
    # GET method
    context = {'form': cls_contactform()}
    return render(request, 'contact/create.html', context) # my_project/contact/templates/contact/create.html