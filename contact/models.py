# my_project/contact/models.py

from django.db import models
from django.utils import timezone

# id (primary key - automatic);
# first_name (string), last_name (string), phone (string), e-mail (email), created_date (date), description (text);
# category (foreing key), show (boolean), owner (foreing key) and picture (image).
class cls_contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    
    show = models.BooleanField(default=True) #
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/') # my_project/media/pictures/

    class Meta: #5: #cls_contact()
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'