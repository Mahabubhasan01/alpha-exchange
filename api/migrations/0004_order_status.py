# Generated by Django 4.0.5 on 2022-08-14 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_review_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='pending', max_length=10),
        ),
    ]
