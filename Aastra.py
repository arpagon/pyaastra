#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       dialbox_recordingproc.py
#       Copyright 2010 arpagon <arpagon@gmail.com.co>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

"""Python Library for admin Aastra Phones
Factory Reset
"""
__version__ = "0.0.1"
__license__ = """The GNU General Public License (GPL-2.0)"""
__author__ = "Sebastian Rojo <http://www.sapian.com.co> arpagon@gamil.com"
__contributors__ = []
_debug = 0

import subprocess
import ping
import logging
import os

logging.basicConfig(level=logging.DEBUG)
if not os.path.exists("/var/log/dialbox"):
    os.makedirs("/var/log/dialbox")
LOG_FILENAME = '/var/log/dialbox/AastraFactoryReset.log'
log = logging.getLogger('AASTRA')
handler = logging.FileHandler(LOG_FILENAME)
handler.setLevel(logging.DEBUG)
log.addHandler(handler)

class Aastra(object):
    '''
    Aastra Class
    '''

    def __init__(self, Ip):
        '''
        Constructor de clase Aastra
        '''
        self.Ip=Ip
        self.Online=None
        self.Mac=None
        self.Ext=None
        self.Register=None
        self.ProvisionFile=None        
        
    def Ping(self):
        return ping.quiet_ping(self.Ip,count=1)
    
    def CheckMac(self):
        result=self.Ping()
        if result[0] == 0:
            log.info("Ip % Online by Ping" % self.Ip)
            p = subprocess.Popen(["arp", "-an", self.Ip], stdout=subprocess.PIpE)
            output, err = p.communicate()
            mac=output.split(" ")[3]
            log.info("The MAC % is this Ip %" % (mac, Ip))
        else:
            log.error("Ip % Offline" % self.Ip)
            
        
    
        