# Generated by Django 5.1.3 on 2024-12-05 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='makananrestoran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NamaMakanan', models.CharField(max_length=100)),
                ('HargaMakanan', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='restoran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namarestoran', models.CharField(max_length=100)),
                ('alamatrestoran', models.CharField(max_length=200)),
            ],
        ),
    ]
