# Generated by Django 3.1.7 on 2021-03-05 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0028_delete_authorizationkey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='automatic_fulfillment_digital_products',
            field=models.BooleanField(default=True),
        ),
    ]
