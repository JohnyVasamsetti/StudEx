# Generated by Django 3.0.2 on 2020-10-02 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200916_1728'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('book', models.FileField(upload_to='books')),
            ],
        ),
    ]
