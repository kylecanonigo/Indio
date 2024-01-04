# Generated by Django 5.0 on 2024-01-02 08:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chapters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameWords',
            fields=[
                ('word_id', models.AutoField(primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=100)),
                ('word_desc', models.TextField()),
                ('is_ans', models.BooleanField()),
                ('chapter_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chapters.chapter')),
            ],
        ),
    ]
