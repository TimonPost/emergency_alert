#!/usr/bin/python
 
 
# P2000 ONTVANGEN OP RASPBERRY PI 2 MET RTL-SDR
# https://nl.oneguyoneblog.com/2016/08/09/p2000-ontvangen-decoderen-raspberry-pi/
#
# vergeet niet deze regel verderop aan te passen aan je eigen RTL-SDR ontvanger (-p en -g):
# multimon_ng = subprocess.Popen("rtl_fm -f 169.65M -M fm -s 22050 -p 43 -g 30 | multimon-ng -a FLEX -t raw -",
 
 
import time
import sys
import subprocess
import os
import re
from datetime import datetime
from dateutil import tz
from termcolor import colored
from enum import Enum
from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer
import Queue
import threading
import urllib2
import json

groupidold = ""
 
def curtime():
    return time.strftime("%H:%M:%S %Y-%m-%d")
 
with open('error.txt','a') as file:
    file.write(('#' * 20) + '\n' + curtime() + '\n')
 
# command for reading certain radio waves. This case 169.65 hz
multimon_ng = subprocess.Popen("rtl_fm -f 169.65M -M fm -s 22050 | multimon-ng -a FLEX -t raw -",
                               stdout=subprocess.PIPE,
                               stderr=open('error.txt','a'),
                               shell=True)

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class SimpleEcho(WebSocket):
    def handleMessage(self):
      if self.data is None:
            self.data = ''
      
      for client in self.server.connections.itervalues():
         if client != self:
            try:
               client.sendMessage(str(self.address[0]) + ' - ' + str(self.data))
            except Exception as n:
               print n


    def handleConnected(self):
        print self.address, 'connected'
          
    def handleClose(self):
        print self.address, 'closed'

echo = SimpleEcho
server = SimpleWebSocketServer('', 8000, echo)

class Pryority (Enum):
    Low = 1
    Medium = 2
    High = 3
    Unknown = 4    

class Message:
     regex_prio1 = "^A\s?1|\s?A\s?1|PRIO\s?1|^P\s?1"
     regex_prio2 = "^A\s?2|\s?A\s?2|PRIO\s?2|^P\s?2"
     regex_prio3 = "^B\s?1|^B\s?2|^B\s?3|PRIO\s?3|^P\s?3|PRIO\s?4|^P\s?4"
          
     def __init__(self, message, capcode, timestamp,flex):
         self.message = message,
         self.capcode = capcode,
         self.timestamp = timestamp,
         self.flex = flex
         print(self.timestamp)
         if re.search(self.regex_prio1, message, re.IGNORECASE):
            self.color = 'red'
            self.prio = Pryority.High
         elif re.search(self.regex_prio2, message, re.IGNORECASE):
            self.color = 'yellow'
            self.prio = Pryority.Medium
         elif re.search(self.regex_prio3, message, re.IGNORECASE):
            self.color = 'green'
            self.prio = Pryority.Low
         else:
            self.color = 'magenta'
            self.prio = Pryority.Unknown          
         
     def draw(self): 
        jsonMessage = Object()
        jsonMessage.message = self.message[0]
        jsonMessage.timestamp = self.timestamp[0]
        jsonMessage.capcode = self.capcode[0]
        jsonMessage.prio =  self.prio.name

        for client in server.connections.itervalues():
             if client != self:
                try:
                    client.sendMessage(jsonMessage.toJSON())
                except Exception as n:
                    print n

        print ' '
        print  colored(self.timestamp[0] ,'blue', attrs=['bold']), colored(self.message[0], self.color,  attrs=['bold']),
        print '                  ',
        print colored(self.capcode[0], 'white'),

    
def start_server():  
    server.serveforever()
         
t = threading.Thread(target=start_server)
t.daemon = True
t.start()

try:
    # an endless loop to read alerts
    while True:
        line = multimon_ng.stdout.readline()
        
        multimon_ng.poll()
        if line.__contains__("ALN"):
		if line.startswith('FLEX'):
                        
			flex = line[0:5]
			timestamp = line[6:25]
			message = line[58:]
			groupid = line[35:41]
			capcode = line[43:52]
                        
                        utc = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
			utc = utc.replace(tzinfo=tz.tzutc())
			local = utc.astimezone(tz.tzlocal())
			local = local.strftime("%d-%m-%Y %H:%M:%S")
                       
                        message = Message(message, capcode, local, flex)                       
                        message.draw()
                        
		if groupid == groupidold: 
			print colored(capcode, 'white'), 
		else:
			groupidold = groupid

except KeyboardInterrupt:
    os.kill(multimon_ng.pid, 9)
