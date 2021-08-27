# Generated by Django 3.2.6 on 2021-08-27 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20210827_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('total_price', models.IntegerField()),
                ('profit', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='salestemp',
            name='profit',
        ),
        migrations.RemoveField(
            model_name='salestemp',
            name='total_price',
        ),
    ]