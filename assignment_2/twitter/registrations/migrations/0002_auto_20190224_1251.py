# Generated by Django 2.1.7 on 2019-02-24 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='end',
            field=models.DateTimeField(null=True),
        ),
    ]
