# Generated by Django 4.1 on 2022-09-13 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0002_alter_project_options_alter_company_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='duration_spent',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
