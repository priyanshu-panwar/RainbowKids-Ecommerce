# Generated by Django 2.2.6 on 2020-03-02 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_auto_20200303_0032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='subcategory',
        ),
    ]
