# Generated by Django 5.0.6 on 2024-07-17 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0011_alter_cls_category_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cls_category',
            old_name='name',
            new_name='name2',
        ),
    ]