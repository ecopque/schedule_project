# Generated by Django 5.0.6 on 2024-07-11 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_rename_create_date_cls_contact_var_createddate_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cls_contact',
            old_name='var_firstname',
            new_name='first_name',
        ),
    ]
