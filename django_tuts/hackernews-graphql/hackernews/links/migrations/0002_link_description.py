# Generated by Django 2.0.4 on 2018-04-24 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
