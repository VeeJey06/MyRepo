# Generated by Django 3.1.1 on 2020-09-18 06:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20200917_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='reading',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]