from django.db import models

# Create your models here.


class Tasktable(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    sn = models.CharField(db_column='SN', max_length=11)
    task = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    # Field name made lowercase.
    starttime = models.DateTimeField(
        db_column='startTime', blank=True, null=True)
    # Field name made lowercase.
    finishtime = models.DateTimeField(
        db_column='finishTime', blank=True, null=True)
    series = models.TextField(blank=True, null=True)
    local_id = models.IntegerField(blank=True, null=True)
    result_id = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'taskTable'


class CatInfo(models.Model):
    # Field name made lowercase.
    platform = models.CharField(
        db_column='Platform', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    sn = models.CharField(db_column='SN', primary_key=True, max_length=11)
    # Field name made lowercase.
    status = models.CharField(
        db_column='STATUS', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    currenttask = models.TextField(
        db_column='CurrentTask', blank=True, null=True)
    # Field name made lowercase.
    os = models.CharField(db_column='OS', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    image = models.CharField(
        db_column='Image', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    bios = models.CharField(
        db_column='BIOS', max_length=30, blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    wlan_module = models.TextField(
        db_column='WLAN Module', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    wlan_driver = models.TextField(
        db_column='WLAN Driver', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    bt_module = models.TextField(db_column='BT Module', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    bt_driver = models.TextField(db_column='BT Driver', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    wwan_module = models.TextField(
        db_column='WWAN Module', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    wwan_driver = models.TextField(
        db_column='WWAN Driver', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    gnss_module = models.TextField(
        db_column='GNSS Module', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    gnss_driver = models.TextField(
        db_column='GNSS Driver', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    nic_module = models.TextField(
        db_column='NIC Module', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    nic_driver = models.TextField(
        db_column='NIC Driver', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    nfc_module = models.TextField(
        db_column='NFC Module', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    nfc_driver = models.TextField(
        db_column='NFC Driver', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    rfid_module = models.TextField(
        db_column='RFID Module', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    rfid_driver = models.TextField(
        db_column='RFID Driver', blank=True, null=True)
    # Field name made lowercase.
    lastusedtime = models.DateTimeField(
        db_column='LastUsedTime', blank=True, null=True)
    # Field name made lowercase.
    tag = models.CharField(
        db_column='Tag', max_length=50, blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    wwan_firmware = models.TextField(
        db_column='WWAN Firmware', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    wwan_modem = models.TextField(
        db_column='WWAN Modem', blank=True, null=True)

    class Meta:
        db_table = 'CAT_info'


class Loglisttable(models.Model):
    # Field name made lowercase.
    id = models.BigAutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    update_time = models.DateTimeField(
        db_column='Update_Time', blank=True, null=True)
    # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=50)
    detail = models.TextField(db_column='Detail')  # Field name made lowercase.
    whitelist = models.BooleanField()
    blacklist = models.BooleanField()
    # Field name made lowercase.
    iseventlogdetail = models.BooleanField(
        db_column='IsEventLogDetail', blank=True, null=True)
    # Field name made lowercase.
    iswwan = models.BooleanField(db_column='IsWWAN', blank=True, null=True)
    # Field name made lowercase.
    iswlan = models.BooleanField(db_column='IsWLAN', blank=True, null=True)
    # Field name made lowercase.
    isnic = models.BooleanField(db_column='IsNIC', blank=True, null=True)
    # Field name made lowercase.
    isnfc = models.BooleanField(db_column='IsNFC', blank=True, null=True)
    # Field name made lowercase.
    isbt = models.BooleanField(db_column='IsBT', blank=True, null=True)
    # Field name made lowercase.
    isgnss = models.BooleanField(db_column='IsGNSS', blank=True, null=True)

    class Meta:
        db_table = 'LogListTable'




class Testlogtable(models.Model):
    # Field name made lowercase.
    id = models.BigAutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    update_time = models.DateTimeField(db_column='Update_Time')
    # Field name made lowercase.
    taskid = models.BigIntegerField(db_column='TaskID', blank=True, null=True)
    # Field name made lowercase.
    localid = models.CharField(
        db_column='LocalID', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    sn = models.CharField(db_column='SN', max_length=100,
                          blank=True, null=True)
    # Field name made lowercase.
    loglistid = models.BigIntegerField(
        db_column='LogListID', blank=True, null=True)
    # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=100)
    # Field name made lowercase.
    eventname = models.CharField(
        db_column='EventName', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    loglevel = models.IntegerField(db_column='LogLevel')
    # Field name made lowercase.
    logleveldisplayname = models.CharField(
        db_column='LogLevelDisplayName', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    timecreated = models.DateTimeField(
        db_column='TimeCreated', blank=True, null=True)
    # Field name made lowercase.
    logid = models.IntegerField(db_column='LogID', blank=True, null=True)
    # Field name made lowercase.
    task = models.IntegerField(db_column='Task', blank=True, null=True)
    # Field name made lowercase.
    processid = models.IntegerField(
        db_column='ProcessID', blank=True, null=True)
    # Field name made lowercase.
    providername = models.TextField(
        db_column='ProviderName', blank=True, null=True)
    # Field name made lowercase.
    count = models.BigIntegerField(db_column='Count', blank=True, null=True)
    # Field name made lowercase.
    detail = models.TextField(db_column='Detail', blank=True, null=True)
    # Field name made lowercase.
    bios = models.CharField(
        db_column='BIOS', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    os = models.CharField(db_column='OS', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    wwan_name = models.CharField(
        db_column='WWAN_Name', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    wwan_driver = models.CharField(
        db_column='WWAN_Driver', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    wwan_fw = models.CharField(
        db_column='WWAN_FW', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    gnss_driver = models.CharField(
        db_column='GNSS_Driver', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    wlan_name = models.CharField(
        db_column='WLAN_Name', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    wlan_driver = models.CharField(
        db_column='WLAN_Driver', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    bt_name = models.CharField(
        db_column='BT_Name', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    bt_driver = models.CharField(
        db_column='BT_Driver', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    nic_name = models.CharField(
        db_column='NIC_Name', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    nic_driver = models.CharField(
        db_column='NIC_Driver', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    nfc_name = models.CharField(
        db_column='NFC_Name', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    nfc_driver = models.CharField(
        db_column='NFC_Driver', max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'TestLogTable'

class Unknowlogtable(models.Model):
        # Field name made lowercase.
    id = models.BigAutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    update_time = models.DateTimeField(
        db_column='Update_Time', blank=True, null=True)
    # Field name made lowercase.
    logtableid = models.BigIntegerField(db_column='LogTableID')
    # Field name made lowercase.
    source = models.CharField(
        db_column='Source', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    eventname = models.CharField(
        db_column='EventName', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    leveldisplayname = models.CharField(
        db_column='LevelDisplayName', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    logid = models.IntegerField(db_column='LogID', blank=True, null=True)
    # Field name made lowercase.
    logtask = models.IntegerField(db_column='LogTask', blank=True, null=True)
    # Field name made lowercase.
    providername = models.TextField(
        db_column='ProviderName', blank=True, null=True)
    # Field name made lowercase.
    count = models.BigIntegerField(db_column='Count', blank=True, null=True)
    # Field name made lowercase.
    detail = models.TextField(db_column='Detail', blank=True, null=True)
    # Field name made lowercase.
    enable = models.BooleanField(db_column='Enable', blank=True, null=True)

    class Meta:
        db_table = 'UnknowLogTable'


class Taskitem(models.Model):
    # Field name made lowercase.
    taskitem = models.TextField(db_column='TaskItem', blank=True, null=True)
    # Field name made lowercase.
    taskindex = models.BigIntegerField(
        db_column='TaskIndex', blank=True, null=True)
    # Field name made lowercase.
    tasktype = models.CharField(
        db_column='TaskType', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    id = models.BigIntegerField(db_column='ID', primary_key=True)

    class Meta:
        managed = False
        db_table = 'TaskItem'


class Catfiles(models.Model):
    stream_id = models.CharField(unique=True, max_length=36)
    file_stream = models.BinaryField(blank=True, null=True)
    name = models.CharField(max_length=255)
    # This field type is a guess.
    path_locator = models.TextField(primary_key=True)
    parent_path_locator = models.ForeignKey(
        'self', models.DO_NOTHING, db_column='parent_path_locator', blank=True, null=True)
    file_type = models.CharField(max_length=255, blank=True, null=True)
    cached_file_size = models.BigIntegerField(blank=True, null=True)
    creation_time = models.TextField()  # This field type is a guess.
    last_write_time = models.TextField()  # This field type is a guess.
    # This field type is a guess.
    last_access_time = models.TextField(blank=True, null=True)
    is_directory = models.BooleanField()
    is_offline = models.BooleanField()
    is_hidden = models.BooleanField()
    is_readonly = models.BooleanField()
    is_archive = models.BooleanField()
    is_system = models.BooleanField()
    is_temporary = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'catfiles'
        unique_together = (('parent_path_locator', 'name'),)
