# Generated by Django 4.2.7 on 2024-07-28 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard', '0006_results'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='heatmap_image',
            field=models.ImageField(blank=True, null=True, upload_to='heatmaps/'),
        ),
    ]
