# Generated by Django 2.2.6 on 2020-03-09 18:22

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_subcategory_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.upload_image_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='image10',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.upload_image_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.upload_image_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.upload_image_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.upload_image_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.upload_image_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='image6',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.upload_image_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='image7',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.upload_image_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='image8',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.upload_image_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='image9',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.upload_image_path),
        ),
    ]
