# Generated by Django 4.0.3 on 2022-05-24 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
