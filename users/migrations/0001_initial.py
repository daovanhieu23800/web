# Generated by Django 3.2 on 2021-11-12 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.PositiveIntegerField()),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('phone', models.PositiveIntegerField(default=0, primary_key=True, serialize=False)),
                ('dateofbirth', models.DateField()),
                ('Address', models.CharField(max_length=50)),
                ('id_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.account')),
            ],
        ),
        migrations.CreateModel(
            name='Credit_card',
            fields=[
                ('id_card', models.PositiveBigIntegerField(default=0, primary_key=True, serialize=False)),
                ('bank', models.CharField(max_length=15)),
                ('expired_day', models.DateTimeField()),
                ('account_name', models.CharField(max_length=100)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.account')),
            ],
        ),
    ]
