# Generated by Django 4.2.3 on 2023-10-30 00:37

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('county_no', models.PositiveSmallIntegerField(unique=True)),
                ('slug', models.SlugField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Counties',
                'db_table': 'counties',
                'ordering': ['county_no'],
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('image', models.ImageField(blank=True, null=True, upload_to='hospital_images')),
                ('license_no', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=254, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('county', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customadmin.county')),
            ],
            options={
                'verbose_name_plural': 'Hospitals',
                'db_table': 'hospitals',
                'ordering': ['name'],
            },
        ),
    ]
