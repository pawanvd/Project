# Generated by Django 4.1.2 on 2022-11-30 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('rno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Manager.rooms')),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('rprice', models.IntegerField()),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manager.category')),
                ('gname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manager.guest')),
            ],
            options={
                'db_table': 'Booking',
            },
        ),
    ]