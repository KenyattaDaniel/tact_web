# Generated by Django 2.0.7 on 2018-12-13 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_package_bill_frequency'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='subtitle',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='service',
            name='subtitle',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]