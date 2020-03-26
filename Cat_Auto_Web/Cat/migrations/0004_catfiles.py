# Generated by Django 2.1.15 on 2020-03-26 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cat', '0003_taskitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catfiles',
            fields=[
                ('stream_id', models.CharField(max_length=36, unique=True)),
                ('file_stream', models.BinaryField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('path_locator', models.TextField(primary_key=True, serialize=False)),
                ('file_type', models.CharField(blank=True, max_length=255, null=True)),
                ('cached_file_size', models.BigIntegerField(blank=True, null=True)),
                ('creation_time', models.TextField()),
                ('last_write_time', models.TextField()),
                ('last_access_time', models.TextField(blank=True, null=True)),
                ('is_directory', models.BooleanField()),
                ('is_offline', models.BooleanField()),
                ('is_hidden', models.BooleanField()),
                ('is_readonly', models.BooleanField()),
                ('is_archive', models.BooleanField()),
                ('is_system', models.BooleanField()),
                ('is_temporary', models.BooleanField()),
            ],
            options={
                'db_table': 'catfiles',
                'managed': False,
            },
        ),
    ]