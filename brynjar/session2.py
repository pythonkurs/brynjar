#/usr/bin/env python
import requests
import untangle



def _get_structure(url):
    req = requests.get(url)
    struct = untangle.parse(req.text)
    return struct

def _get_escalators_counts(struct):
    esc = []
    esc_repair = []
    for outage in struct.NYCOutages.outage:
        if outage.equipmenttype=="ES":
            esc.append(outage)
            if outage.reason == "REPAIR":
                esc_repair.append(outage)

    
    return (len(esc_repair),len(esc))

def _get_esc_repair_frac(url):
    struct = _get_structure(url)
    (esc_repair,esc_tot) = _get_escalators_counts(struct)
    return float(esc_repair)/float(esc_tot)
    

def get_esc_repair_frac_NYCT():
    url = "http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml"
    return _get_esc_repair_frac(url)
