# Generated by Django 2.1.7 on 2019-04-28 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadapp', '0002_auto_20190429_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='emoji',
            name='photoID',
            field=models.IntegerField(default=0),
        ),
    ]
