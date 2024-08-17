# Generated by Django 5.0.1 on 2024-08-13 06:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images_mode', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageBackup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.ImageField(upload_to='images_backup/')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images_backup', to='images_mode.category')),
            ],
        ),
    ]
