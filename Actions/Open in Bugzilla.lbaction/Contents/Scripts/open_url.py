#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Pavel Miroshnichenko"
__email__ = "facetheheat@icloud.com"

import os
import os.path
import sys
import subprocess
import json
import plistlib

supportPath = os.environ.get('LB_SUPPORT_PATH')
settingsPath = supportPath + "/Preferences.plist"


def openTicket(ticket):
    bugzillaUrlFile = plistlib.readPlist(settingsPath)
    bugzillaUrl = bugzillaUrlFile.get('Bugzilla URL')
    if bugzillaUrl:
        cmd = ["open", bugzillaUrl + "/show_bug.cgi?id=" + ticket]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (output, error_output) = proc.communicate()
        return 0
    else:
        print 'Error in Preferences.plist. File was Removed'
        cmd = ["rm", settingsPath]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (output, error_output) = proc.communicate()
    return 0


def createSettingsFile():
    d = {'Bugzilla URL':"http://server.com/bugzilla",}
    settingsFile = open(settingsPath,'w')
    try:
        plistlib.writePlist(d, settingsFile)
        settingsFile.seek(0)
    finally:
        settingsFile.close()
    return 0


def main():
    if os.path.isfile(settingsPath):
        inputArguments = json.loads(sys.argv[1])
        for item in inputArguments:
            openTicket(item.keys()[0])
    else:
        createSettingsFile()
        openSettingsFile = {}
        openSettingsFile['title'] = 'Bugzilla URL is not set. Type ENTER'
        openSettingsFile['subtitle'] = 'in Preferences.plist'
        openSettingsFile['path'] = "%s" % settingsPath
        print json.dumps(openSettingsFile)
    return 0

# Start program
if __name__ == "__main__":
    main()
