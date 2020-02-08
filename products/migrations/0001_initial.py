# Generated by Django 2.1 on 2020-02-04 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=255)),
                ('product_name', models.CharField(max_length=255)),
                ('product_price', models.FloatField()),
                ('image_url', models.CharField(max_length=2083)),
            ],
        ),
    ]
