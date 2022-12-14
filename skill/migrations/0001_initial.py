# Generated by Django 4.1 on 2022-09-11 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SkillSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_title', models.CharField(max_length=100)),
                ('proficiency', models.FloatField()),
                ('relevant_experience', models.IntegerField()),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skill.skill')),
            ],
        ),
    ]
