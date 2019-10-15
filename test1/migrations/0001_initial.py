# Generated by Django 2.2.3 on 2019-08-02 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='university',
            fields=[
                ('u_id', models.AutoField(primary_key=True, serialize=False)),
                ('u_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'university',
            },
        ),
        migrations.CreateModel(
            name='weather_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('ET', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('EP', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('BSS', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('RF', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('WD', models.CharField(max_length=50)),
                ('WD1', models.CharField(max_length=50)),
                ('WS', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('DT1', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('WT1', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('DT2', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('WT2', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('MAXT', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('MINT', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('RH11', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('RH22', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('VP11', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('VP22', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('CLOUDM', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('CLOUDE', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('SOIL1', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('SOIL2', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('SOIL3', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('SOIL4', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('SOIL5', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('SOIL6', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('MinTtest', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('MaxTtest1', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('MaxTtest2', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
            options={
                'db_table': 'weather_data',
            },
        ),
    ]
