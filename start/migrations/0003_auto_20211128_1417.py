# Generated by Django 3.2.6 on 2021-11-28 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0002_rename_height_detail_depth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detail',
            old_name='price',
            new_name='price1',
        ),
        migrations.AddField(
            model_name='detail',
            name='price2',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
    ]
