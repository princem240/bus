# Generated by Django 4.2 on 2023-07-09 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_book_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='duration',
            field=models.CharField(default='1', max_length=50),
        ),
    ]
