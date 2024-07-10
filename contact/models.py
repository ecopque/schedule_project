# my_project/contact/models.py

from django.db import models
from django.utils import timezone

# id (primary key - automatic);
# first_name (string), last_name (string), phone (string), e-mail (email), created_date (date), description (text), category (foreing key), show (boolean), owner (foreing key) and picture (image).
class cls_contact(models.Model):
    var_firstname = models.CharField(name='First Name', max_length=50)
    var_lastname = models.CharField(name='Last Name', max_length=50, blank=True)
    var_phone = models.CharField(name='Phone Number', max_length=20)
    var_email = models.EmailField(name='E-mail', max_length=254)
    var_createddate = models.DateTimeField(name='Create Date', default=timezone.now)
    var_description = models.TextField(name='Description', blank=True)

    class Meta: #cls_contact()
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'