# Generated by Django 5.0.6 on 2024-07-10 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cls_contact',
            old_name='var_description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='cls_contact',
            old_name='var_email',
            new_name='E-mail',
        ),
        migrations.RenameField(
            model_name='cls_contact',
            old_name='var_firstname',
            new_name='First Name',
        ),
        migrations.RenameField(
            model_name='cls_contact',
            old_name='var_lastname',
            new_name='Last Name',
        ),
        migrations.RenameField(
            model_name='cls_contact',
            old_name='var_phone',
            new_name='Phone Number',
        ),
    ]