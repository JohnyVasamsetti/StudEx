# Generated by Django 3.0.2 on 2020-10-01 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ID_NO',
            field=models.CharField(default=None, max_length=7),
        ),
    ]
