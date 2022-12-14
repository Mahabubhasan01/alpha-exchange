# Generated by Django 4.0.5 on 2022-08-12 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('send_method', models.CharField(choices=[('Bkash', 'Bkash'), ('Nagad', 'Nagad'), ('Rocket', 'Rocket'), ('Upay', 'Upay'), ('Visa/Master card', 'Visa/Master card')], max_length=100)),
                ('receive_method', models.CharField(choices=[('Bkash', 'Bkash'), ('Nagad', 'Nagad'), ('Rocket', 'Rocket'), ('Upay', 'Upay'), ('Visa/Master card', 'Visa/Master card')], max_length=100)),
                ('send_amount', models.PositiveIntegerField()),
                ('receive_amount', models.PositiveIntegerField()),
                ('send_number', models.IntegerField()),
                ('receive_number', models.IntegerField()),
                ('contact_number', models.IntegerField()),
            ],
        ),
    ]
