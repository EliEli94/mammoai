# Generated by Django 4.2.7 on 2024-07-28 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard', '0003_patient_pid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='breast_health',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='medical_history',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='risk_assessment_form',
        ),
        migrations.AddField(
            model_name='patient',
            name='age_first_birth',
            field=models.PositiveIntegerField(blank=True, choices=[(0, '<20 years'), (1, '20-24 years'), (2, '25-29 years'), (3, '>= 30 years'), (4, 'Nulliparous'), (9, 'Unknown')], null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='age_menarche',
            field=models.PositiveIntegerField(blank=True, choices=[(0, '>14 years'), (1, '12-13 years'), (2, '<12 years'), (9, 'Unknown')], null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='birads_breast_density',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'Almost entirely fatty'), (2, 'Scattered areas of fibroglandular density'), (3, 'Heterogeneously dense'), (4, 'Extremely dense'), (9, 'Unknown')], null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='breast_cancer_history',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 'No history'), (1, 'Yes, history of breast cancer'), (9, 'Unknown')], null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='current_hrt',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 'No current HRT'), (1, 'Yes, current HRT'), (9, 'Unknown')], null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='first_degree_hx',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes'), (9, 'Unknown')], null=True),
        ),
    ]
