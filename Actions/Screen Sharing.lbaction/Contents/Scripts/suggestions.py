#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Pavel Miroshnichenko"
__email__ = "pavel@miroshnichen.co"

import os
import sys
import plistlib
import re
import json

def fetch_hosts_from_vncloc():
    hosts = []
    for root, dirs, files in os.walk(history_folder):
        for file in files:
            if file.endswith(".vncloc"):
                hostPrefs = {}
                filePath = root + file
                connection_name = plistlib.readPlist(filePath)
                connection_name = connection_name['URL']
                hostPrefs['title'] = connection_name[6::]
                hostPrefs['icon'] = 'com.apple.ScreenSharing'
                hostPrefs['subtitle'] = 'connect to vnc://%s via Screen Sharing.app' % hostPrefs['title']
                hosts.append(hostPrefs)
    #creating filtered list
    filtered_hosts = []
    for element in hosts:
        match = re.match(host, element['title'])
        if match:
            filtered_hosts.append(element)
    return filtered_hosts

if __name__ == "__main__":
    user_name = os.getlogin()
    history_folder = ('/Users/'+ user_name +'/Library/Application Support/Screen Sharing/')
    if len(sys.argv) == 2:
        host = sys.argv[1]
        if host.startswith('vnc://'):
            host = host[6::]
    else:
        host = ''
    print json.dumps(fetch_hosts_from_vncloc())