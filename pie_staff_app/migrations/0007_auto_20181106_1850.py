# Generated by Django 2.1.1 on 2018-11-06 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pie_staff_app', '0006_pieuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='pie_staff_app.PieUser'),
        ),
        migrations.AddField(
            model_name='snippet',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='snippet',
            name='name',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
    ]
