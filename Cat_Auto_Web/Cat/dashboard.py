from django.views.generic import ListView 
from Cat.models import CatInfo
from Cat.models import Erdtable
import re

def list_uut(**kwargs):
    if kwargs:
        sn = kwargs['sn']
        platform = kwargs['platform']
        tag = kwargs['tag']
        if sn:
            catinfo = list(CatInfo.objects.filter(sn__contains=sn).values().order_by('-lastusedtime'))
        elif platform:
            catinfo = list(CatInfo.objects.filter(platform__contains=platform).values().order_by('-lastusedtime'))
        elif tag:
            catinfo = list(CatInfo.objects.filter(tag__contains=tag).values().order_by('-lastusedtime')) 
        else:
            catinfo = list(CatInfo.objects.all().values().order_by('-lastusedtime'))
    else:
        catinfo = list(CatInfo.objects.all().values().order_by('-lastusedtime'))

    erdtable_modules_hwid = Erdtable.objects.all().values('short_name', 'vender_id', 'device_id', 'subsys_vender_id', 'subsys_device_id')

    def hwid_split(hwid):
        spliters_layer1 = ['\\\\', '&']
        spliters_layer2 = ['VEN','DEV','PID','VID','SUBSYS','NXP']

        if hwid:
            hwid_temp = hwid
            try:
                hwid = re.split('['+'|'.join(spliters_layer1)+']', hwid)
                hwid = [_h for _h in hwid if any(__h in _h for __h in spliters_layer2)]
                hwid = [_h.replace('NXP','NXP_') if 'NXP' in _h else _h for _h in hwid]
                hwid = [_h[_h.index('_')+1:] for _h in hwid]
            except TypeError as error:
                print(hwid_temp)
                print(error.args)
            if not hwid:
                return hwid_temp
            return hwid
        else:
            return None

    def hwid_convertto_shortname(hwid_split_list):
        if len(hwid_split_list)<2:
            return None
        short_name = [device['short_name'] for device in erdtable_modules_hwid if ((device['vender_id'] == hwid_split_list[0]) and (device['device_id'] == hwid_split_list[1]))]
        if not any(short_name):
            return None
        return short_name
    # convert cat_info hwid to erdtable short name
    def update_short_name(_catinfo):
        
        for i, uut in enumerate(_catinfo):
            _catinfo[i]['status'] = _catinfo[i]['status'].strip()
            wlan = uut['wlan_module']
            bt = uut['bt_module']
            nic = uut['nic_module']
            nfc = uut['nfc_module']
            rfid = uut['rfid_module']
            wwan = uut['wwan_module']
            if wlan != 'NA':
                wlan_short_name = hwid_convertto_shortname(hwid_split(wlan))
                if wlan_short_name:
                    _catinfo[i]['wlan_module'] = wlan_short_name[0]
            if bt != 'NA':
                bt_short_name = hwid_convertto_shortname(hwid_split(bt))
                if bt_short_name:
                    _catinfo[i]['bt_module'] = bt_short_name[0]
            if nic != 'NA':
                nic_short_name = hwid_convertto_shortname(hwid_split(nic))
                if nic_short_name:
                    _catinfo[i]['nic_module'] = nic_short_name[0]
            if wwan != 'NA':
                wwan_short_name = hwid_convertto_shortname(hwid_split(wwan))
                if wwan_short_name:
                    _catinfo[i]['wwan_module'] = wwan_short_name[0]
            if nfc != 'NA':
                nfc_short_name = hwid_convertto_shortname(hwid_split(nfc))
                if nfc_short_name:
                    _catinfo[i]['nfc_module'] = nfc_short_name[0]
            if rfid != 'NA':
                rfid_short_name = hwid_convertto_shortname(hwid_split(rfid))
                if rfid_short_name:
                    _catinfo[i]['rfid_module'] = rfid_short_name[0]
        return _catinfo
        
    return update_short_name(catinfo)



# class UUTListView(ListView):
#     model = CatInfo

#     def get_context_data(self, **kwargs):
#         context = super(UUTListView, self).get_context_data(**kwargs)
#         return context


# dashboard_uut_list = UUTListView.as_view(
#     queryset=catinfo,
#     context_object_name='uut_list',
#     template_name='Cat/dashboard.html',
# )
