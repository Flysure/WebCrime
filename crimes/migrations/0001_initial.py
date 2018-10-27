# Generated by Django 2.1.2 on 2018-10-27 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrimeTable',
            fields=[
                ('field1', models.TextField(blank=True, null=True)),
                ('crnumber', models.TextField(blank=True, db_column='CRnumber', primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
                ('victim', models.TextField(blank=True, db_column='Victim', null=True)),
                ('datereported', models.TextField(blank=True, db_column='DateReported', null=True)),
                ('location', models.TextField(blank=True, db_column='Location', null=True)),
                ('lat', models.TextField(blank=True, db_column='Lat', null=True)),
                ('lng', models.TextField(blank=True, db_column='Lng', null=True)),
            ],
            options={
                'db_table': 'crime_table',
                'managed': False,
            },
        ),
    ]