# Generated by Django 5.0.6 on 2024-07-10 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_rename_var_description_cls_contact_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cls_contact',
            old_name='var_createddate',
            new_name='Create Date',
        ),
    ]
