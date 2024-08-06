# my_project/contact/forms.py

from django import forms
from django.core.exceptions import ValidationError
from contact.models import cls_contact # my_project/contact/models.py

class cls_contactform(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['first_name'].widget.attrs.update({'class': 'class-a class-b', 'placeholder': 'Write here 2',}) # substituted

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'class-a class-b', 'placeholder': 'Write here3',}), label='First Nameee', help_text='Help text.') # my_project/contact/templates/contact/create.html

    class Meta:
        model = cls_contact
        fields = ('first_name', 'last_name', 'phone',)

        # widgets = {'first_name': forms.PasswordInput(), 'last_name': forms.TextInput(attrs={'class': 'class-a class-b', 'placeholder': 'Write here',}), 'phone': forms.Textarea()} # substituted

    def clean(self):
        cleaned_data = self.cleaned_data
        # self.add_error('first_name', ValidationError('Error message.', code='invalid')) # analysis
        first_name = cleaned_data.get('first_name') ##
        last_name = cleaned_data.get('last_name') ##
        if first_name == last_name: ##
            msg_error = ValidationError('First name cannot be the same as second name.', code='invalid')
            self.add_error('first_name', msg_error) ##
            self.add_error('last_name', msg_error) ##
        return super().clean() ##

    def clean_first_name(self): ## #1:
        first_name = self.cleaned_data.get('first_name')
        print('def clean_first_name: print.')
        if first_name == 'ABC': ##
            raise ValidationError('Shit! Do not enter ABC in this field.', code='invalid') #2: ##
            # self.add_error('first_name', ValidationError('Error message.', code='invalid')) #3: ##
        return first_name