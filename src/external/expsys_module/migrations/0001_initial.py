# Generated by Django 5.1.4 on 2025-04-01 14:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Competence_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sat_coef', models.FloatField(default=0)),
                ('competence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expsys_module.competence')),
                ('subject', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='lms.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Skill_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sat_coef', models.FloatField(default=0)),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expsys_module.skill')),
                ('subject', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='lms.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Vacance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('salary_from', models.FloatField(default=0)),
                ('salary_to', models.FloatField(default=0)),
                ('currency', models.CharField(default='', max_length=255)),
                ('area', models.CharField(default='', max_length=255)),
                ('type', models.CharField(default='', max_length=255)),
                ('employment', models.CharField(default='', max_length=255)),
                ('experience', models.CharField(default='', max_length=255)),
                ('skill', models.ManyToManyField(related_name='vacance_skill', to='expsys_module.skill')),
            ],
        ),
    ]
