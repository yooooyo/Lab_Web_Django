from django.contrib import admin
from Cat import models
# Register your models here.
class CatInfoAdmin(admin.ModelAdmin):
    list_display = ['platform','sn','status','currenttask','os','image','bios','lastusedtime']
    list_filter = list_display.copy()
    search_fields = list_display.copy()

class TaskTableAdmin(admin.ModelAdmin):
    list_display = ['id','sn','task','state','result','starttime','finishtime','series','local_id','result_id','ap']
    list_filter = list_display.copy()
    search_fields = list_display.copy()

class ERDTableAdmin(admin.ModelAdmin):
    list_display = ['id','deliverables_name','short_name','owner','vender_id','device_id','subsys_vender_id','subsys_device_id']
    list_filter = list_display.copy()
    search_fields = list_display.copy()



class TestScriptsAdmin(admin.ModelAdmin):
    list_display = ['name','tool','wwan','wlan','lan']
    list_filter = list_display.copy()
    search_fields = list_display.copy()
    actions=['set_tool_pvt','set_tool_pws','clear_tool','set_type_wwan','clear_type_wwan','set_type_wlan','clear_type_wlan','set_type_lan','clear_type_lan',]

    def set_tool_pvt(self, request, queryset):
        queryset.update(tool='winpvt')
    set_tool_pvt.short_description = "+ tool winpvt"

    def set_tool_pws(self, request, queryset):
        queryset.update(tool='powerstress')
    set_tool_pws.short_description = "+ tool powerstress"

    def clear_tool(self, request, queryset):
        queryset.update(type=None)
    clear_tool.short_description = "- Tool"

    def set_type_wwan(self, request, queryset):
        queryset.update(wwan=True)
    set_type_wwan.short_description = "+ wwan"

    def clear_type_wwan(self, request, queryset):
        queryset.update(wwan=None)
    clear_type_wwan.short_description = "- wwan"

    def set_type_wlan(self, request, queryset):
        queryset.update(wlan=True)
    set_type_wlan.short_description = "+ wlan"

    def clear_type_wlan(self, request, queryset):
        queryset.update(wlan=None)
    clear_type_wlan.short_description = "- wlan"

    def set_type_lan(self, request, queryset):
        queryset.update(lan=True)
    set_type_lan.short_description = "+ lan"

    def clear_type_lan(self, request, queryset):
        queryset.update(lan=None)
    clear_type_lan.short_description = "- lan"

    def set_type_bt(self, request, queryset):
        queryset.update(bt=True)
    set_type_bt.short_description = "Set type As BT"

    def clear_type_bt(self, request, queryset):
        queryset.update(bt=None)
    clear_type_bt.short_description = "Clear type BT"

    def set_type_nfc(self, request, queryset):
        queryset.update(nfc=True)
    set_type_nfc.short_description = "Set type As NFC"

    def clear_type_nfc(self, request, queryset):
        queryset.update(nfc=None)
    clear_type_nfc.short_description = "Clear type NFC"

    def set_type_rfid(self, request, queryset):
        queryset.update(rfid=True)
    set_type_rfid.short_description = "Set type As RFID"

    def clear_type_rfid(self, request, queryset):
        queryset.update(rfid=None)
    clear_type_rfid.short_description = "Clear type RFID"

    # def make_published(self, request, queryset):
    #     updated = queryset.update(status='p')
    #     self.message_user(request, ngettext(
    #         '%d story was successfully marked as published.',
    #         '%d stories were successfully marked as published.',
    #         updated,
    #     ) % updated, messages.SUCCESS)
    
class APTableAdmin(admin.ModelAdmin):
    list_display = ['no','type','platform','vender','select','cycles','cpu','wi1_chip1','wi1_protocols','wi1_chip2','wi2_protocols','support_lte','number_5g','network_technology_standard','adapter','location','status','admin_id','admin_pw','ssid','pw','ssid_5g','pw1','number_2_4g_bssid','number_2_4g_band','number_5g_bssid','number_5g_band','fw_version','remark','f30','active']
    list_filter = list_display.copy()
    search_fields = list_display.copy()
    actions = ['active']
    def active(self, request, queryset):
        queryset.update(active=True)
    active.short_description = "active"

admin.site.register(models.CatInfo,CatInfoAdmin)
admin.site.register(models.Tasktable,TaskTableAdmin)
admin.site.register(models.Erdtable,ERDTableAdmin)
admin.site.register(models.TestScripts,TestScriptsAdmin)
admin.site.register(models.Ap,APTableAdmin)