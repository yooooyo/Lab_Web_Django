from Cat.models import CatInfo
from Cat.models import Erdtable
from django.views.generic import ListView 
import re

catinfo = list(CatInfo.objects.all().values().order_by('-lastusedtime'))
erdtable_modules_hwid = Erdtable.objects.all().values('short_name', 'vender_id', 'device_id', 'subsys_vender_id', 'subsys_device_id')

def hwid_split(hwid):
    spliters_layer1 = ['\\\\', '&']
    spliters_layer2 = ['VEN','DEV','PID','VID','SUBSYS','NXP']
    hwid_temp = hwid
    hwid = re.split('['+'|'.join(spliters_layer1)+']', hwid)
    hwid = [_h for _h in hwid if any(__h in _h for __h in spliters_layer2)]
    hwid = [_h.replace('NXP','NXP_') if 'NXP' in _h else _h for _h in hwid]
    hwid = [_h[_h.index('_')+1:] for _h in hwid]
    if not hwid:
        return hwid_temp
    return hwid


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
        

catinfo = update_short_name(catinfo)



class UUTListView(ListView):
    model = CatInfo

    def get_context_data(self, **kwargs):
        context = super(UUTListView, self).get_context_data(**kwargs)
        return context


dashboard_uut_list = UUTListView.as_view(
    queryset=catinfo,
    context_object_name='uut_list',
    template_name='Cat/dashboard.html',
)
