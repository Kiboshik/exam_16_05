# Generated by Django 3.2 on 2022-05-18 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='examapp.post'),
        ),
    ]
