# Generated by Django 4.2.6 on 2023-10-27 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=20)),
                ('time_period', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='timings',
            field=models.ManyToManyField(to='homepage.timing'),
        ),
    ]
