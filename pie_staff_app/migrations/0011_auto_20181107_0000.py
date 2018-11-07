# Generated by Django 2.1.1 on 2018-11-07 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pie_staff_app', '0010_auto_20181106_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('completed', models.BooleanField(default=False)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pie_staff_app.PieUser')),
            ],
        ),
        migrations.AddField(
            model_name='pieuser',
            name='assignedIssues',
            field=models.ManyToManyField(to='pie_staff_app.Issue'),
        ),
    ]