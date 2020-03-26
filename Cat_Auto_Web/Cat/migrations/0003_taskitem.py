# Generated by Django 2.1.15 on 2020-03-26 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cat', '0002_catinfo_loglisttable_testlogtable_unknowlogtable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taskitem',
            fields=[
                ('taskitem', models.TextField(blank=True, db_column='TaskItem', null=True)),
                ('taskindex', models.BigIntegerField(blank=True, db_column='TaskIndex', null=True)),
                ('tasktype', models.CharField(blank=True, db_column='TaskType', max_length=30, null=True)),
                ('id', models.BigIntegerField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'TaskItem',
                'managed': False,
            },
        ),
    ]