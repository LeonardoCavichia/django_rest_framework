# Generated by Django 2.2.6 on 2019-11-11 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_eventos', '0018_auto_20191110_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='sex',
            field=models.CharField(max_length=1),
        ),
    ]
