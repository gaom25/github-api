# Generated by Django 3.1 on 2020-09-09 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='githubuser',
            name='name',
            field=models.CharField(default='', max_length=250, null=True, verbose_name='name'),
        ),
    ]