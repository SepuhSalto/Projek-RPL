# Generated by Django 5.1.3 on 2024-12-16 17:25

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
                ('idlocation', models.BigAutoField(primary_key=True, serialize=False)),
                ('lokasi', models.CharField(max_length=50)),
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
                ('handphone', models.CharField(blank=True, max_length=15)),
                ('alamat', models.TextField(blank=True)),
                ('foto_profil', models.ImageField(blank=True, default='images/default.jpg', upload_to='images/')),
                ('foto_background', models.ImageField(blank=True, default='images/default.jpg', upload_to='images/')),
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
                ('foto', models.ImageField(blank=True, default='images/default.jpg', upload_to='images/')),
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
                ('foto', models.ImageField(blank=True, default='images/default.jpg', upload_to='images/')),
                ('rating_count', models.IntegerField(default=0)),
                ('Deskripsi', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('idkategori', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='crud.kategori')),
                ('idrestoran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.restoran')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('idrating', models.BigAutoField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('foto', models.ImageField(blank=True, default='default.jpg', upload_to='images/')),
                ('video', models.FileField(blank=True, upload_to='videos/')),
                ('komentar', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('idmenu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.menu')),
                ('idpengguna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.users')),
            ],
        ),
    ]
