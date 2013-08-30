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

from optparse import OptionParser
from mechanize import Browser
import subprocess
import ping
import logging

logging.basicConfig(level=logging.DEBUG)
if not os.path.exists("/var/log/dialbox"):
    os.makedirs("/var/log/dialbox")
LOG_FILENAME = '/var/log/dialbox/AastraFactoryReset.log'
log = logging.getLogger('AASTRARESET')
handler = logging.FileHandler(LOG_FILENAME)
handler.setLevel(logging.DEBUG)
log.addHandler(handler)

def Ping(ip):
    return ping.quiet_ping(ip,count=1)
    
def CheckProvisionFile(ip):
    result=Ping(ip)
    if result[0] == 0:
        log.info("IP % Online by Ping" % ip)
        p = subprocess.Popen(["arp", "-an", ip], stdout=subprocess.PIPE)
        output, err = p.communicate()
        mac=output.split(" ")[3]
        log.info("The MAC % is this IP %" % (mac, ip))
    else:
        og.error("IP % Offline" % ip)
    

def FactoryReset(url_aastra):
    br = Browser()
    br.add_password(url_aastra, "admin", "22222")
    br.open(url_aastra + "/reset.html")
    br.select_form(nr=0)
    c=br.form.controls[3]
    c.readonly=False
    br.form["resetOption"]="1"
    response=br.submit()
    print response.read()

def Reset(url_aastra):
    br = Browser()
    br.add_password(url_aastra, "admin", "22222")
    br.open(url_aastra + "/reset.html")
    br.select_form(nr=0)
    c=br.form.controls[3]
    c.readonly=False
    br.form["resetOption"]="0"
    response=br.submit()
    print response.read()

def RemoveLocalConfig(url_aastra):
    br = Browser()
    br.add_password(url_aastra, "admin", "22222")
    br.open(url_aastra + "/reset.html")
    br.select_form(nr=0)
    c=br.form.controls[3]
    c.readonly=False
    br.form["resetOption"]="2"
    response=br.submit()
    print response.read()

if __name__=='__main__':
    main()