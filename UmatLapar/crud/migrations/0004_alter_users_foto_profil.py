# Generated by Django 5.1.3 on 2024-12-13 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_alter_rating_foto_alter_users_foto_profil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='foto_profil',
            field=models.ImageField(blank=True, default='images/default.jpg', upload_to='images/'),
        ),
    ]
