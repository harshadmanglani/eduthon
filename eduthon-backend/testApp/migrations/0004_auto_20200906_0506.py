# Generated by Django 3.1.1 on 2020-09-05 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0003_auto_20200905_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]