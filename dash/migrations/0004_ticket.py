# Generated by Django 3.2.9 on 2021-12-22 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dash', '0003_auto_20211221_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount', models.IntegerField(default=0)),
                ('ref_no', models.CharField(max_length=25)),
                ('accepted', models.BooleanField(default=False)),
                ('remarks', models.CharField(max_length=100)),
                ('response', models.CharField(default='', max_length=200)),
                ('roll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
