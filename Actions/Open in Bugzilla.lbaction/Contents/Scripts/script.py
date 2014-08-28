#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Pavel Miroshnichenko"
__email__ = "facetheheat@icloud.com"

import sys
import subprocess
import re
import json
import time

inputString = sys.argv[1]
ticketsList = re.sub('[A-z.,\:-_=+%$^#{}\'\"/]', '', inputString)
ticketsList = ticketsList.split(' ')

items = []
openAll = {}
openAll['title'] = 'Open All'
openAll['icon'] = 'Safari.png'
openAll['action'] = 'open_url.py'
argumentList = []
for everyTicket in ticketsList:
    outputArguments = {}
    outputArguments[everyTicket] = everyTicket
    argumentList.append(outputArguments)
    openAll['actionArgument'] = json.dumps(argumentList)
items.append(openAll)

for ticket in ticketsList:
    item = {}
    item['title'] = ticket
    item['subtitle'] = "Open ticket in a browser..."
    item['icon'] = 'Documents.png'
    item['action'] = 'open_url.py'
    outputArguments = {}
    outputArguments[ticket] = ticket
    item['actionArgument'] = json.dumps([outputArguments])
    items.append(item)

print json.dumps(items)
