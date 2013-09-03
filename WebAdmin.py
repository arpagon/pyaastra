#!/usr/bin/env python2.6
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

activate_this = "/opt/DialBox/bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))

from optparse import OptionParser
from mechanize import Browser
import subprocess
import ping
import logging
import os

logging.basicConfig(level=logging.DEBUG)
if not os.path.exists("/var/log/dialbox"):
    os.makedirs("/var/log/dialbox")
LOG_FILENAME = '/var/log/dialbox/AastraFactoryReset.log'
log = logging.getLogger('AASTRAWEB')
handler = logging.FileHandler(LOG_FILENAME)
handler.setLevel(logging.DEBUG)
log.addHandler(handler)

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
    resetOption=br.form.controls[3]
    resetOption.readonly=False
    br.form["resetOption"]="2"
    response=br.submit()
    print response.read()
    
def GetLocalConfigFile(url_aastra, return_file):
    br = Browser()
    br.add_password(url_aastra, "admin", "22222")
    try:
        br.retrieve(url_aastra + "/localcfg.html", return_file)
    except:
        log.warn("Maybe isn't a aastra phone? You are Sure?")

def GetServerConfigFile(url_aastra, return_file):
    br = Browser()
    br.add_password(url_aastra, "admin", "22222")
    try:
        br.retrieve(url_aastra + "/servercfg.html", return_file)
    except:
        log.warn("Maybe isn't a aastra phone? You are Sure?")
    
def main():
    pass

if __name__=='__main__':
    main()