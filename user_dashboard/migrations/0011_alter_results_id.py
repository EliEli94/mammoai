# Generated by Django 4.2.7 on 2024-07-28 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard', '0010_results_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]