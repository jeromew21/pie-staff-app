# Generated by Django 2.1.1 on 2018-11-06 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pie_staff_app', '0008_auto_20181106_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pie_staff_app.PieUser'),
        ),
    ]
