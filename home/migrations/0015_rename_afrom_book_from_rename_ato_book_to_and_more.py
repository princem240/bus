# Generated by Django 4.2 on 2023-07-14 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_book_from_remove_book_to_remove_book_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='aFrom',
            new_name='From',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='aTo',
            new_name='To',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='adate',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='aname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='aprice',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='atimefrom',
            new_name='timefrom',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='atimeto',
            new_name='timeto',
        ),
    ]
