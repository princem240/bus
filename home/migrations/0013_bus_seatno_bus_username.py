# Generated by Django 4.2 on 2023-07-10 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0012_alter_book_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='seatno',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bus',
            name='username',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]