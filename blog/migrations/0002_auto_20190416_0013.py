# Generated by Django 2.1.7 on 2019-04-16 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='foto',
            field=models.ImageField(upload_to=''),
        ),
    ]
