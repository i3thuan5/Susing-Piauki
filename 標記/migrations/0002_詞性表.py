# Generated by Django 2.0.2 on 2018-05-25 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('標記', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='詞性表',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('詞性', models.CharField(max_length=30, unique=True)),
                ('華文解釋', models.TextField(blank=True)),
                ('英文解釋', models.TextField(blank=True)),
                ('備註', models.TextField(blank=True)),
            ],
        ),
    ]
