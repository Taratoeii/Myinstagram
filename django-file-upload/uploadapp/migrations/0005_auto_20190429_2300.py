# Generated by Django 2.1.7 on 2019-04-29 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadapp', '0004_remove_comment_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='emoji',
            name='emoji',
            field=models.TextField(null=True),
        ),
    ]
