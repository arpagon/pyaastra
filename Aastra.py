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

    def __init__(self, IP):
        '''
        Constructor de clase Aastra
        '''
        self.IP=IP
        self.Online=None
        self.MAC=None
        self.Ext=None
        self.Register=None
        self.ProvisionFile=None

        
    def Ping(self):
        return ping.quiet_ping(self.IP,count=1)
    
    def CheckMac(self):
        result=self.Ping()
        if result[0] == 0:
            log.info("IP %s Online by Ping" % self.IP)
            p = subprocess.Popen(["arp", "-an", self.IP], stdout=subprocess.PIPE)
            output, err = p.communicate()
            self.MAC=output.split(" ")[3]
            self.ProvisionFile("/tftpboot/" + self.MAC)
            log.info("The MAC %s is this IP %s" % (self.MAC, self.IP))
        else:
            log.error("IP %s Offline" % self.IP)
            
class ProvisionFile(object):
    '''
    Provisioning Class
    '''

    def __init__(self, FilePath):
        '''
        Constructor de clase ProfisionFile
        '''
        self.Path=FilePath
        self.Exist=None
        self.IsOK=None
        self.Length=None
        self.CheckProvisioningFile()
    
    def CheckProvisioningFile(self):
        self.Exist=os.path.isfile(self.Path)
        if self.Exist:
            self.Length=__file_len(self.Path)
            if self.Length >= 10:
                self.IsOK=True
            else:
                self.IsOK=False
        else:
            self.IsOK=False
    

def __file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
    
            
        
    
        