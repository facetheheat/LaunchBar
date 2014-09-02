#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Pavel Miroshnichenko"
__email__ = "facetheheat@icloud.com"

import sys
import subprocess
import re
import json

#Create unsorted output from disk utility
#skips first 9 lines of the output
cmd = ["/usr/sbin/diskutil", "listFilesystems"]
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(output, error_output) = proc.communicate()
output = output.split('\n')[9:]

#Create list of filesystems
listFilesystems = []
for row in output:
    row = row.strip()
    match = re.search("\(or\)", row, re.I | re.S | re.M)
    if match or row == "":
        continue
    row = row.split('  ')
    if row[0] == 'Free Space':
        continue
    listFilesystems.append(row[0])

items = []
for fs in listFilesystems:
    item = {}
    item['title'] = fs
    item['subtitle'] = "Create %s RAM Drive" % fs
    if fs == 'MS-DOS' or fs == 'MS-DOS FAT32' or fs == 'MS-DOS FAT12' or fs == 'MS-DOS FAT16':
        item['icon'] = 'fat.png'
    elif fs == 'ExFAT':
        item['icon'] = 'exfat.png'
    elif fs == 'UFSD_NTFS' or fs == 'UFSD_NTFSCOMPR' or fs == 'Tuxera NTFS':
        item['icon'] = 'ntfs.png'
    elif fs == 'UFSD_EXTFS' or fs == 'UFSD_EXTFS3' or fs == 'UFSD_EXTFS4':
        item['icon'] = 'extfs.png'
    elif fs == 'HFS+' or fs == 'Journaled HFS+' or 'Case-sensitive HFS+' or 'Case-sensitive Journaled HFS+':
        item['icon'] = 'hfs.png'
    else:
        item['icon'] = 'default.png'
    item['action'] = 'createVolume.py'
    item['actionReturnsItems'] = True
    outputArguments = {}
    outputArguments['volumeSize'] = "%s" % sys.argv[1]
    outputArguments['filesystemType'] = "%s" % fs
    item['actionArgument'] = json.dumps(outputArguments)
    items.append(item)
print json.dumps(items)
