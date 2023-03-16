# Generated by Django 4.1.2 on 2022-11-27 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('gname', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=20)),
                ('uidno', models.IntegerField()),
                ('contactno', models.IntegerField()),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Guest',
            },
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rno', models.IntegerField()),
                ('rimage', models.ImageField(default='abc.jpg', upload_to='Images')),
                ('rprice', models.IntegerField()),
                ('rdescription', models.CharField(max_length=1000)),
                ('rservices', models.CharField(max_length=500)),
                ('ravailability', models.CharField(choices=[('AVB', 'Available'), ('UAVB', 'Unavailable')], default='AVB', max_length=20)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manager.category')),
            ],
            options={
                'db_table': 'Rooms',
            },
        ),
    ]