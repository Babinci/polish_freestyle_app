# Generated by Django 5.0.1 on 2024-08-14 06:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images_mode', '0003_maincategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='main_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='images_mode.maincategory'),
        ),
    ]
