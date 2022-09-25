# Generated by Django 4.1 on 2022-09-11 15:17

from django.db import migrations, models
import intro.utils


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('description', models.TextField()),
                ('extra_circular_activities', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='introduction',
            name='image',
            field=models.ImageField(upload_to=intro.utils.upload_to),
        ),
    ]