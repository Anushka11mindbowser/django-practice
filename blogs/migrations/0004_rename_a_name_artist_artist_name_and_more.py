# Generated by Django 4.0.4 on 2022-05-27 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_demo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='a_name',
            new_name='artist_name',
        ),
        migrations.RenameField(
            model_name='band',
            old_name='a_name',
            new_name='artist_name',
        ),
        migrations.RenameField(
            model_name='band',
            old_name='b_name',
            new_name='band_name',
        ),
        migrations.RenameField(
            model_name='membership',
            old_name='a_name',
            new_name='artist_name',
        ),
        migrations.RenameField(
            model_name='membership',
            old_name='b_name',
            new_name='band_name',
        ),
    ]
