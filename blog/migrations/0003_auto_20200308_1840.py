# Generated by Django 3.0.3 on 2020-03-08 17:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20200308_1546'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPost',
            new_name='Blog',
        ),
    ]
