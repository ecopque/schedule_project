from django.db import models
from django.utils import timezone

# Create your models here.

# id (primary key - automatic);
# first_name (string), last_name (string), phone (string), e-mail (email), created_date (date), description (text), category (foreing key), show (boolean), owner (foreing key) and picture (image).
class cls_contact(models.Model):
    var_firstname = models.CharField(max_length=50)
    var_lastname = models.CharField(max_length=50, blank=True)
    var_phone = models.CharField(max_length=20)
    var_email = models.EmailField(max_length=254)
    var_createddate = models.DateTimeField(default=timezone.now)