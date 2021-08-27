# Generated by Django 3.2.6 on 2021-08-27 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesTemp',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('purchase_price', models.IntegerField()),
                ('sale_price', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('profit', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='products',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]