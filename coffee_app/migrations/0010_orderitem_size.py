# Generated by Django 3.2 on 2021-12-08 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_app', '0009_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='size',
            field=models.CharField(default='s', max_length=1),
        ),
    ]