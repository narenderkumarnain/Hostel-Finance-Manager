# Generated by Django 3.2.9 on 2021-12-22 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0005_auto_20211222_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='accepted',
            field=models.CharField(choices=[('RJ', 'Rejected'), ('AA', 'Accepted'), ('PS', 'Processing')], default='PS', max_length=2),
        ),
    ]
