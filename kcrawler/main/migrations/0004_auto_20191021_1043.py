# Generated by Django 2.2.6 on 2019-10-21 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20191021_1035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articleitem',
            name='article',
        ),
        migrations.AddField(
            model_name='articleitem',
            name='headline',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articleitem',
            name='url',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
    ]
