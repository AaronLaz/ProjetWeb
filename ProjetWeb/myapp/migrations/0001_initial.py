# Generated by Django 3.0.3 on 2020-03-03 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postName', models.CharField(blank=True, max_length=20)),
                ('postDate', models.DateTimeField()),
            ],
            options={
                'db_table': 'blogpost',
            },
        ),
        migrations.CreateModel(
            name='Scramble',
            fields=[
                ('scrambleID', models.AutoField(primary_key=True, serialize=False)),
                ('scrambleLength', models.IntegerField()),
                ('scramble', models.CharField(blank=True, max_length=45)),
            ],
            options={
                'db_table': 'scramble',
            },
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puzzleType', models.CharField(choices=[('2', '2x2'), ('3', '3x3'), ('4', '4x4'), ('5', '5x5')], max_length=10)),
                ('best', models.BigIntegerField(blank=True)),
                ('average', models.BigIntegerField(blank=True)),
                ('worst', models.BigIntegerField(blank=True)),
            ],
            options={
                'db_table': 'statistic',
            },
        ),
    ]