# Generated by Django 3.2.8 on 2021-10-30 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='total_items',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]