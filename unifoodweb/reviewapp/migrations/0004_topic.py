# Generated by Django 2.0 on 2018-02-03 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewapp', '0003_util'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('sentiment', models.TextField(blank=True, null=True)),
                ('words', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'topic',
                'managed': False,
            },
        ),
    ]
