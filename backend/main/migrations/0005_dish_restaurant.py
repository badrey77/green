# Generated by Django 4.2.4 on 2023-08-28 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_restaurantofman'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='restaurant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='main.restaurant'),
            preserve_default=False,
        ),
    ]
