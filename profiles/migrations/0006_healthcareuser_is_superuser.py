# Generated by Django 3.0.8 on 2020-07-05 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_add_provinces'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthcareuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]