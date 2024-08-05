# my_project/contact/forms.py

from django import forms
from django.core.exceptions import ValidationError
from contact.models import cls_contact # my_project/contact/models.py

class cls_contactform(forms.ModelForm):
    class Meta:
        model = cls_contact
        fields = ('first_name', 'last_name', 'phone',) ##

        widgets = {'first_name': forms.PasswordInput()} ##
        widgets = {'phone': forms.Textarea()} ##

    def clean(self):
        # cleaned_data = self.cleaned_data
        self.add_error('first_name', ValidationError('Error message.', code='invalid'))
        return super().clean()