# Generated by Django 3.2.6 on 2021-08-26 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Shopping Bag', 'Shopping Bag'), ('Card', 'Card'), ('Box', 'Box')], max_length=200)),
                ('purpose', models.CharField(choices=[('Corporate Gifts', 'Corporate Gifts'), ('HR', 'HR'), ('Packaging', 'Packaging')], max_length=200)),
                ('quantity', models.IntegerField(blank=True, default=1)),
                ('length', models.IntegerField(blank=True, default=0)),
                ('width', models.IntegerField(blank=True, default=0)),
                ('height', models.IntegerField(blank=True, default=0)),
                ('budget', models.CharField(choices=[('Budget Friendly', 'Budget Friendly'), ('Best Rated', 'Best Rated'), ('Moderately Priced', 'Moderately Priced'), ('Good Quality', 'Good Quality'), ('Exotic', 'Exotic')], max_length=200)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Details_of_Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(max_length=42)),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('purpose', models.CharField(max_length=200)),
                ('budget', models.CharField(max_length=200)),
            ],
        ),
    ]