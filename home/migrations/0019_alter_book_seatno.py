# Generated by Django 4.2 on 2023-07-24 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_book_busid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='seatno',
            field=models.CharField(default=1, max_length=50),
        ),
    ]
