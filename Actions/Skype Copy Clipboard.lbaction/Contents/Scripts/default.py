#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Pavel Miroshnichenko"
__email__ = "pavel@miroshnichen.co"

import sys
import re
from subprocess import Popen, PIPE

cmd = '/usr/bin/osascript "./friends.scpt"'
p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
out, err = p.communicate()
text = out.split(',')
for item in text:
    item = item.split(';')
    display_name = item[0].strip()
    account_name = item[1].strip()
    search_name = sys.argv[1]
    match = re.search(account_name, search_name)
    if match:
        cmd = 'echo "%s, skype: %s" |pbcopy' % (display_name, account_name)
        p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
