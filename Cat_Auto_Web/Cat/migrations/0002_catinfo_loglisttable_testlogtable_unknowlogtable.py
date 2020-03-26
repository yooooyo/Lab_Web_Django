# Generated by Django 2.1.15 on 2020-03-26 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatInfo',
            fields=[
                ('platform', models.CharField(blank=True, db_column='Platform', max_length=50, null=True)),
                ('sn', models.CharField(db_column='SN', max_length=11, primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, db_column='STATUS', max_length=20, null=True)),
                ('currenttask', models.TextField(blank=True, db_column='CurrentTask', null=True)),
                ('os', models.CharField(blank=True, db_column='OS', max_length=30, null=True)),
                ('image', models.CharField(blank=True, db_column='Image', max_length=30, null=True)),
                ('bios', models.CharField(blank=True, db_column='BIOS', max_length=30, null=True)),
                ('wlan_module', models.TextField(blank=True, db_column='WLAN Module', null=True)),
                ('wlan_driver', models.TextField(blank=True, db_column='WLAN Driver', null=True)),
                ('bt_module', models.TextField(blank=True, db_column='BT Module', null=True)),
                ('bt_driver', models.TextField(blank=True, db_column='BT Driver', null=True)),
                ('wwan_module', models.TextField(blank=True, db_column='WWAN Module', null=True)),
                ('wwan_driver', models.TextField(blank=True, db_column='WWAN Driver', null=True)),
                ('gnss_module', models.TextField(blank=True, db_column='GNSS Module', null=True)),
                ('gnss_driver', models.TextField(blank=True, db_column='GNSS Driver', null=True)),
                ('nic_module', models.TextField(blank=True, db_column='NIC Module', null=True)),
                ('nic_driver', models.TextField(blank=True, db_column='NIC Driver', null=True)),
                ('nfc_module', models.TextField(blank=True, db_column='NFC Module', null=True)),
                ('nfc_driver', models.TextField(blank=True, db_column='NFC Driver', null=True)),
                ('rfid_module', models.TextField(blank=True, db_column='RFID Module', null=True)),
                ('rfid_driver', models.TextField(blank=True, db_column='RFID Driver', null=True)),
                ('lastusedtime', models.DateTimeField(blank=True, db_column='LastUsedTime', null=True)),
                ('tag', models.CharField(blank=True, db_column='Tag', max_length=50, null=True)),
                ('wwan_firmware', models.TextField(blank=True, db_column='WWAN Firmware', null=True)),
                ('wwan_modem', models.TextField(blank=True, db_column='WWAN Modem', null=True)),
            ],
            options={
                'db_table': 'CAT_info',
            },
        ),
        migrations.CreateModel(
            name='Loglisttable',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('update_time', models.DateTimeField(blank=True, db_column='Update_Time', null=True)),
                ('source', models.CharField(db_column='Source', max_length=50)),
                ('detail', models.TextField(db_column='Detail')),
                ('whitelist', models.BooleanField()),
                ('blacklist', models.BooleanField()),
                ('iseventlogdetail', models.BooleanField(blank=True, db_column='IsEventLogDetail', null=True)),
                ('iswwan', models.BooleanField(blank=True, db_column='IsWWAN', null=True)),
                ('iswlan', models.BooleanField(blank=True, db_column='IsWLAN', null=True)),
                ('isnic', models.BooleanField(blank=True, db_column='IsNIC', null=True)),
                ('isnfc', models.BooleanField(blank=True, db_column='IsNFC', null=True)),
                ('isbt', models.BooleanField(blank=True, db_column='IsBT', null=True)),
                ('isgnss', models.BooleanField(blank=True, db_column='IsGNSS', null=True)),
            ],
            options={
                'db_table': 'LogListTable',
            },
        ),
        migrations.CreateModel(
            name='Testlogtable',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('update_time', models.DateTimeField(db_column='Update_Time')),
                ('taskid', models.BigIntegerField(blank=True, db_column='TaskID', null=True)),
                ('localid', models.CharField(blank=True, db_column='LocalID', max_length=100, null=True)),
                ('sn', models.CharField(blank=True, db_column='SN', max_length=100, null=True)),
                ('loglistid', models.BigIntegerField(blank=True, db_column='LogListID', null=True)),
                ('source', models.CharField(db_column='Source', max_length=100)),
                ('eventname', models.CharField(blank=True, db_column='EventName', max_length=100, null=True)),
                ('loglevel', models.IntegerField(db_column='LogLevel')),
                ('logleveldisplayname', models.CharField(blank=True, db_column='LogLevelDisplayName', max_length=100, null=True)),
                ('timecreated', models.DateTimeField(blank=True, db_column='TimeCreated', null=True)),
                ('logid', models.IntegerField(blank=True, db_column='LogID', null=True)),
                ('task', models.IntegerField(blank=True, db_column='Task', null=True)),
                ('processid', models.IntegerField(blank=True, db_column='ProcessID', null=True)),
                ('providername', models.TextField(blank=True, db_column='ProviderName', null=True)),
                ('count', models.BigIntegerField(blank=True, db_column='Count', null=True)),
                ('detail', models.TextField(blank=True, db_column='Detail', null=True)),
                ('bios', models.CharField(blank=True, db_column='BIOS', max_length=50, null=True)),
                ('os', models.CharField(blank=True, db_column='OS', max_length=50, null=True)),
                ('wwan_name', models.CharField(blank=True, db_column='WWAN_Name', max_length=100, null=True)),
                ('wwan_driver', models.CharField(blank=True, db_column='WWAN_Driver', max_length=50, null=True)),
                ('wwan_fw', models.CharField(blank=True, db_column='WWAN_FW', max_length=100, null=True)),
                ('gnss_driver', models.CharField(blank=True, db_column='GNSS_Driver', max_length=50, null=True)),
                ('wlan_name', models.CharField(blank=True, db_column='WLAN_Name', max_length=100, null=True)),
                ('wlan_driver', models.CharField(blank=True, db_column='WLAN_Driver', max_length=50, null=True)),
                ('bt_name', models.CharField(blank=True, db_column='BT_Name', max_length=100, null=True)),
                ('bt_driver', models.CharField(blank=True, db_column='BT_Driver', max_length=50, null=True)),
                ('nic_name', models.CharField(blank=True, db_column='NIC_Name', max_length=100, null=True)),
                ('nic_driver', models.CharField(blank=True, db_column='NIC_Driver', max_length=50, null=True)),
                ('nfc_name', models.CharField(blank=True, db_column='NFC_Name', max_length=100, null=True)),
                ('nfc_driver', models.CharField(blank=True, db_column='NFC_Driver', max_length=50, null=True)),
            ],
            options={
                'db_table': 'TestLogTable',
            },
        ),
        migrations.CreateModel(
            name='Unknowlogtable',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('update_time', models.DateTimeField(blank=True, db_column='Update_Time', null=True)),
                ('logtableid', models.BigIntegerField(db_column='LogTableID')),
                ('source', models.CharField(blank=True, db_column='Source', max_length=200, null=True)),
                ('eventname', models.CharField(blank=True, db_column='EventName', max_length=200, null=True)),
                ('leveldisplayname', models.CharField(blank=True, db_column='LevelDisplayName', max_length=200, null=True)),
                ('logid', models.IntegerField(blank=True, db_column='LogID', null=True)),
                ('logtask', models.IntegerField(blank=True, db_column='LogTask', null=True)),
                ('providername', models.TextField(blank=True, db_column='ProviderName', null=True)),
                ('count', models.BigIntegerField(blank=True, db_column='Count', null=True)),
                ('detail', models.TextField(blank=True, db_column='Detail', null=True)),
                ('enable', models.BooleanField(blank=True, db_column='Enable', null=True)),
            ],
            options={
                'db_table': 'UnknowLogTable',
            },
        ),
    ]
