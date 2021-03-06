# Generated by Django 3.1.7 on 2021-03-05 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0141_update_descritpion_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digitalcontent',
            name='automatic_fulfillment',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='digitalcontent',
            name='content_file',
            field=models.FileField(blank=True, default='shop.gethookedseafood.com', upload_to='digital_contents'),
        ),
        migrations.AlterField(
            model_name='digitalcontent',
            name='max_downloads',
            field=models.IntegerField(blank=True, default=10, null=True),
        ),
        migrations.AlterField(
            model_name='digitalcontent',
            name='url_valid_days',
            field=models.IntegerField(blank=True, default=10, null=True),
        ),
        migrations.AlterField(
            model_name='digitalcontent',
            name='use_default_settings',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='is_digital',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='is_shipping_required',
            field=models.BooleanField(default=False),
        ),
    ]