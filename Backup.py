#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       backup.py
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
backup
"""
__version__ = "0.0.1"
__license__ = """The GNU General Public License (GPL-2.0)"""
__author__ = "Sebastian Rojo <http://www.sapian.com.co> arpagon@gamil.com"
__contributors__ = []
_debug = 0

import logging
import os
from datetime import datetime
from Aastra import Aastra
import shutil
import WebAdmin

logging.basicConfig(level=logging.DEBUG)
if not os.path.exists("/var/log/dialbox"):
    os.makedirs("/var/log/dialbox")
LOG_FILENAME = '/var/log/dialbox/AastraFactoryReset.log'
log = logging.getLogger('AASTRABACKUP')
handler = logging.FileHandler(LOG_FILENAME)
handler.setLevel(logging.DEBUG)
log.addHandler(handler)

BackupDir="/home/backup/Aastra/"

def BackupPhone(IP, BackupDir=BackupDir):
    log.info("backup for phone %s" % IP)
    Date=datetime.now().strftime("%Y-%M-%d")
    BackupDirWhitDate=BackupDir + Date
    log.info("backup dir is %s" % BackupDirWhitDate)
    if not os.path.exists(BackupDirWhitDate):
        os.makedirs(BackupDirWhitDate)
    Phone=Aastra(IP)
    Phone.CheckMac()
    if Phone.ProvisionFile.Exist:
        log.info("Copy Provision File in Server: %s to %s" % (Phone.ProvisionFile.Path, BackupDirWhitDate))
        shutil.copy(Phone.ProvisionFile.Path, BackupDirWhitDate)
    else:
        log.warn("In server Provision File Dont Exist")
    if Phone.Online:
        log.info("Online Phone Try Get Local And Server Config From Phone")
        aastra_url="http://" + IP
        local_config_file=BackupDirWhitDate + "/" + Phone.MAC + "local.cfg"
        remote_server_file=BackupDirWhitDate + "/" + Phone.MAC + "server.cfg"
        log.info("Get Remote: Local Config File on %s" % local_config_file)
        WebAdmin.GetLocalConfigFile(aastra_url, local_config_file)
        log.info("Get Remote: Server Config File on %s" % remote_server_file)
        WebAdmin.GetServerConfigFile(aastra_url, remote_server_file)
    

def main():
    pass

if __name__=='__main__':
    main()