# Generated by Django 3.1rc1 on 2020-08-17 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_add_more_provinces'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthcareprovince',
            name='api_key',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
