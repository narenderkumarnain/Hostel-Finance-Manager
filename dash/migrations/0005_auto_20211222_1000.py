# Generated by Django 3.2.9 on 2021-12-22 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0004_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='remarks',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='response',
            field=models.TextField(default='', max_length=200),
        ),
    ]
