# my_project/contact/forms.py
# Create contacts: http://127.0.0.1:8000/contacts/create/

from django import forms
from django.core.exceptions import ValidationError
from contact.models import cls_contact # my_project/contact/models.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation


class cls_contactform(forms.ModelForm):
    # first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'class-a class-b', 'placeholder': 'Write here3',}), label='First Nameee', help_text='Help text.') # my_project/contact/templates/contact/create.html
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['first_name'].widget.attrs.update({'class': 'class-a class-b', 'placeholder': 'Write here 2',}) # substituted

    picture = forms.ImageField(widget=forms.FileInput(attrs={'accept': 'image/*',}))
    class Meta:
        model = cls_contact
        fields = ('first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture',)

        # widgets = {'first_name': forms.PasswordInput(), 'last_name': forms.TextInput(attrs={'class': 'class-a class-b', 'placeholder': 'Write here',}), 'phone': forms.Textarea()} # substituted

    def clean(self):
        cleaned_data = self.cleaned_data
        # self.add_error('first_name', ValidationError('Error message.', code='invalid')) # analysis
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg_error = ValidationError('First name cannot be the same as second name.', code='invalid')
            self.add_error('first_name', msg_error)
            self.add_error('last_name', msg_error)
        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        print('def clean_first_name: print.')
        if first_name == 'ABC':
            raise ValidationError('Shit! Do not enter ABC in this field.', code='invalid')
            # self.add_error('first_name', ValidationError('Error message.', code='invalid'))
        return first_name
    
class cls_registerform(UserCreationForm):
    first_name = forms.CharField(required=True, min_length=3, error_messages={'required': 'Se fudeu!'})
    last_name = forms.CharField(required=True, min_length=3)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error('email', ValidationError('This e-mail already exists.', code='invalid'),)
        return email
    
class cls_registerupdateform(forms.ModelForm):
    first_name = forms.CharField(min_length=2, max_length=30, required=True, help_text='Required, mdf!', error_messages={'min_length': 'Please, add more than 2 letters.'},)

    last_name = forms.CharField(min_length=2, max_length=30, required=True, help_text='Required, sob!',)

    password1 = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}), help_text=password_validation.password_validators_help_text_html(), required=False,)
    
    password2 = forms.CharField(label="Password 2", strip=False, widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}), help_text='Use the same password as before.', required=False,)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email
        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error('email', ValidationError('This e-mail already exists.', code='invalid'),)
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error('password', ValidationError(errors))
        return password1