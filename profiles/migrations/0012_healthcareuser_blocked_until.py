# Generated by Django 3.1 on 2020-09-02 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_auto_20200831_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthcareuser',
            name='blocked_until',
            field=models.DateTimeField(help_text='If set, the user will be blocked until that time.', null=True),
        ),
    ]
