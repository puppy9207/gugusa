# Generated by Django 3.0.1 on 2019-12-26 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='user_no',
        ),
        migrations.AddField(
            model_name='account',
            name='user_id',
            field=models.CharField(max_length=100, null='false'),
            preserve_default='false',
        ),
        migrations.AlterField(
            model_name='account',
            name='user_type',
            field=models.IntegerField(),
        ),
    ]