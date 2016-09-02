# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 22:05:27 2016

@author: areed145
"""

import aprslib
import datetime
#import pandas as pd
#import matplotlib as mpl

callsign = 'KK6GPV'

def record(text):
    with open(str(callsign)+'.txt', "a") as myfile:
        myfile.write(text)

def callback(packet):
    if packet.get('from') == callsign:
        print(str(packet.get('from'))+' - '+str(datetime.datetime.utcnow().strftime("%d-%m-%Y %H:%M:%S"))+' - '+str(packet.get('latitude'))+' / '+str(packet.get('longitude'))+' / '+str(packet.get('altitude'))+' / '+str(packet.get('speed')))
        text = str(packet.get('from'))+', '+str(datetime.datetime.utcnow().strftime("%d-%m-%Y %H:%M:%S"))+', '+str(packet.get('latitude'))+', '+str(packet.get('longitude'))+', '+str(packet.get('altitude'))+', '+str(packet.get('speed'))+'\n'
        record(text)

AIS = aprslib.IS('KK6GPV')
AIS.connect()
# by default `raw` is False, then each line is ran through aprslib.parse()
AIS.consumer(callback, raw=False)