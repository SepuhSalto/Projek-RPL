# Generated by Django 5.1.3 on 2024-12-11 13:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kategori',
            fields=[
                ('idkategori', models.BigAutoField(primary_key=True, serialize=False)),
                ('kategori', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('idlocation', models.BigAutoField(default=1, primary_key=True, serialize=False)),
                ('lokasi', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('idpengguna', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='John Doe', max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('poin', models.IntegerField(default=0)),
                ('hobi', models.TextField(blank=True)),
                ('pekerjaan', models.TextField(blank=True, max_length=100)),
                ('alamat', models.TextField(blank=True)),
                ('foto_profil', models.ImageField(blank=True, upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restoran',
            fields=[
                ('idrestoran', models.BigAutoField(primary_key=True, serialize=False)),
                ('namaRestoran', models.CharField(max_length=50)),
                ('waktuBuka', models.TimeField()),
                ('waktuTutup', models.TimeField()),
                ('alamat', models.TextField()),
                ('foto', models.ImageField(blank=True, upload_to='images/')),
                ('hargaTerkecil', models.IntegerField()),
                ('hargaTerbesar', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('idlocation', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='crud.location')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('idmenu', models.BigAutoField(primary_key=True, serialize=False)),
                ('namaMenu', models.CharField(max_length=50)),
                ('foto', models.ImageField(blank=True, upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('idkategori', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='crud.kategori')),
                ('idrestoran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.restoran')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('idevent', models.BigAutoField(primary_key=True, serialize=False)),
                ('namaevent', models.CharField(max_length=50)),
                ('deskripsi', models.TextField()),
                ('tanggal', models.DateField()),
                ('lokasi', models.TextField()),
                ('foto', models.ImageField(blank=True, upload_to='images/')),
                ('video', models.FileField(blank=True, upload_to='videos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('idrestoran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.restoran')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('idrating', models.BigAutoField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('foto', models.ImageField(blank=True, upload_to='images/')),
                ('video', models.FileField(blank=True, upload_to='videos/')),
                ('komentar', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('idmenu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.menu')),
                ('idpengguna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.users')),
            ],
        ),
    ]
