# my_project/contact/forms.py

from django import forms
from django.core.exceptions import ValidationError
from contact.models import cls_contact # my_project/contact/models.py

class cls_contactform(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['first_name'].widget.attrs.update({'class': 'class-a class-b', 'placeholder': 'Write here 2',})

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'class-a class-b', 'placeholder': 'Write here3',}), label='First Nameee', help_text='Help text.') # my_project/contact/templates/contact/create.html

    class Meta:
        model = cls_contact
        fields = ('first_name', 'last_name', 'phone',)

        # widgets = {'first_name': forms.PasswordInput(), 'last_name': forms.TextInput(attrs={'class': 'class-a class-b', 'placeholder': 'Write here',}), 'phone': forms.Textarea()}

    def clean(self):
        # cleaned_data = self.cleaned_data
        # self.add_error('first_name', ValidationError('Error message.', code='invalid'))
        return super().clean()

    def clean_first_name(self): #1:
        first_name = self.cleaned_data.get('first_name')
        print('def clean_first_name: print.')
        return first_name
