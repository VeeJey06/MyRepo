# Generated by Django 3.1.1 on 2020-09-17 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20200916_2301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answers',
            old_name='answer1',
            new_name='familyinfected',
        ),
        migrations.RenameField(
            model_name='answers',
            old_name='answer2',
            new_name='heartpatient',
        ),
        migrations.RenameField(
            model_name='answers',
            old_name='answer3',
            new_name='travelhistory',
        ),
    ]
