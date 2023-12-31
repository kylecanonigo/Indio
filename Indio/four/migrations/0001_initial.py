# Generated by Django 4.2.7 on 2023-12-30 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chapters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FourPicsOneWord',
            fields=[
                ('game_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=1000)),
                ('correct_answer', models.CharField(max_length=255)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chapters.lessons')),
            ],
        ),
    ]
