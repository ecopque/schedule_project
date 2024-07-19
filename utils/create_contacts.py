import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice
import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 1000

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False

django.setup()

if __name__ =='__main__':
    import faker
    from contact.models import cls_category, cls_contact

    cls_contact.objects.all().delete()
    cls_category.objects.all().delete()

    fake = faker.Faker('pt_BR')
    categories = ['Friends', 'Family', 'Acquaintances']

    django_categories = [cls_category(name=name) for name in categories]
    for category in django_categories:
        category.save()
    
    django_contacts = []
    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        email = profile['mail']
        first_name, last_name = profile['name'].split(' ', 1)
        phone = fake.phone_number()
        create_date: datetime = fake.date_this_year()
        description = random_text = fake.text(max_nb_chars=100)
        category = choice(django_categories)
        (...)