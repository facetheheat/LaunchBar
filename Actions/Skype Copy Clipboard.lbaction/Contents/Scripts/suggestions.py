#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Pavel Miroshnichenko"
__email__ = "pavel@miroshnichen.co"

import sys
import re
import json
from subprocess import Popen, PIPE

def get_():
    cmd = '/usr/bin/osascript "./friends.scpt"'
    p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    text = out.split(',')
    friends = []
    for item in text:
        item = item.split(';')
        friend_properties = {}
        friend_properties['title'] = item[0].strip()
        friend_properties['icon'] = 'com.skype.skype'
        friend_properties['subtitle'] = item[1].strip()
        friend_properties['action'] = 'default.py'
        friend_properties['actionArgument'] = json.dumps(item[1].strip())
        friends.append(friend_properties)

    filtered_text = []
    for element in friends:
        match = re.search(friend.decode('utf-8').lower(), element['title'].decode('utf-8').lower())
        if match:
            filtered_text.append(element)
    return filtered_text

if __name__ == "__main__":
    if len(sys.argv) == 2:
        friend = sys.argv[1]
    print json.dumps(get_())