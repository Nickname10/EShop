# Generated by Django 3.0.3 on 2020-03-17 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_profile_prof_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='prof_email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sur_name',
        ),
    ]
