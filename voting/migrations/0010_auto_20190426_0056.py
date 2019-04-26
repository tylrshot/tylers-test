# Generated by Django 2.2 on 2019-04-26 00:56

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('voting', '0009_auto_20190421_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gradeLevel', models.IntegerField(blank=True)),
                ('votedIN', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=0), blank=True, null=True, size=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='poll',
            name='description',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.DeleteModel(
            name='UserVotes',
        ),
    ]
