# Generated by Django 2.1.7 on 2019-04-29 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploadapp', '0005_auto_20190429_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='photoID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploadapp.Photo'),
        ),
    ]
