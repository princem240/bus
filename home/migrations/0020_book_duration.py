# Generated by Django 4.2 on 2023-07-25 03:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_book_seatno'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='duration',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]