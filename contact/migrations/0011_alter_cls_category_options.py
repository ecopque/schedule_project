# Generated by Django 5.0.6 on 2024-07-15 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0010_cls_category_cls_contact_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cls_category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
