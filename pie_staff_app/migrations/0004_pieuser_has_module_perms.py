# Generated by Django 2.1.1 on 2018-11-06 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pie_staff_app', '0003_auto_20181106_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='pieuser',
            name='has_module_perms',
            field=models.BooleanField(default=False),
        ),
    ]
