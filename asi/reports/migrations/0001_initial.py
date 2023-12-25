# Generated by Django 4.2.8 on 2023-12-23 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InputData',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('temperature', models.IntegerField(default=0)),
                ('weigth', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('surname', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ReportInputData',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('idInputData', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.inputdata')),
                ('idRerport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.report')),
            ],
        ),
    ]
