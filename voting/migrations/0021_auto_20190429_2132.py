# Generated by Django 2.2 on 2019-04-30 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0020_auto_20190429_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='students',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]