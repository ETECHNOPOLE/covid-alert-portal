# Generated by Django 3.1.5 on 2021-01-22 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0018_add_new_province_alter_province_abbr'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthcareprovince',
            name='sms_enabled',
            field=models.BooleanField(default=False),
        ),
    ]
