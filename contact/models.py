# my_project/contact/models.py

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #

# id (primary key - automatic);
# first_name (string), last_name (string), phone (string), e-mail (email), created_date (date), description (text);
# category (foreing key), show (boolean), owner (foreing key) and picture (image).

class cls_category(models.Model):
    name = models.CharField(max_length=50)

    class Meta: # #cls_category()
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name

class cls_contact(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First Name')
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20) # verbose_name = 'Phone Number'
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/') # my_project/media/pictures/
    category = models.ForeignKey(cls_category, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta: #cls_contact()
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True) #
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'