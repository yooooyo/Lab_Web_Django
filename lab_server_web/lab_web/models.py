# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CatInfo(models.Model):
    platform = models.CharField(db_column='Platform', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sn = models.CharField(db_column='SN', primary_key=True, max_length=11)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    currenttask = models.TextField(db_column='CurrentTask', blank=True, null=True)  # Field name made lowercase.
    os = models.CharField(db_column='OS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bios = models.CharField(db_column='BIOS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wlan_module = models.TextField(db_column='WLAN Module', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wlan_driver = models.TextField(db_column='WLAN Driver', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bt_module = models.TextField(db_column='BT Module', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bt_driver = models.TextField(db_column='BT Driver', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wwan_module = models.TextField(db_column='WWAN Module', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wwan_driver = models.TextField(db_column='WWAN Driver', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gnss_module = models.TextField(db_column='GNSS Module', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gnss_driver = models.TextField(db_column='GNSS Driver', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nic_module = models.TextField(db_column='NIC Module', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nic_driver = models.TextField(db_column='NIC Driver', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nfc_module = models.TextField(db_column='NFC Module', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nfc_driver = models.TextField(db_column='NFC Driver', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rfid_module = models.TextField(db_column='RFID Module', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rfid_driver = models.TextField(db_column='RFID Driver', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lastusedtime = models.DateTimeField(db_column='LastUsedTime', blank=True, null=True)  # Field name made lowercase.
    tag = models.CharField(db_column='Tag', max_length=50, blank=True, null=True)  # Field name made lowercase.
    wwan_firmware = models.TextField(db_column='WWAN Firmware', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wwan_modem = models.TextField(db_column='WWAN Modem', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'cat_info'
