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
 
 # gets the current time
def curtime():
    return time.strftime("%H:%M:%S %Y-%m-%d")
 
with open('error.txt','a') as file:
    file.write(('#' * 20) + '\n' + curtime() + '\n')
 
# command for reading certain radio waves. This case 169.65 hz.
# mutimon writes the input =
# when error occurs it will be written to error.txt
multimon_ng = subprocess.Popen("rtl_fm -f 169.65M -M fm -s 22050 | multimon-ng -a FLEX -t raw -",
                               stdout=subprocess.PIPE,
                               stderr=open('error.txt','a'),
                               shell=True)

# this class could be used to create json objects with.
class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class WebSocketAlert(WebSocket):
    def handleMessage(self):
      if self.data is None:
            self.data = ''
      # loop trough all connections
      for client in self.server.connections.itervalues():
         if client != self:
            try:
               # send message to connected client (brouwser)
               client.sendMessage(str(self.address[0]) + ' - ' + str(self.data))
            except Exception as n:
               print n

    # will be executed when a client connects to websocket
    def handleConnected(self):
        print self.address, 'connected'
    # will be executed when client closes connection with or websocket.
    def handleClose(self):
        print self.address, 'closed'

# init server at port 8000 and local IP address
server = SimpleWebSocketServer('', 8000, WebSocketAlert)

# Pryority of alert
class Pryority (Enum):
    Low = 1
    Medium = 2
    High = 3
    Unknown = 4
       
# The message we receive from the sensor
class Message:
     # regexes to filter prios from message
     regex_prio1 = "^A\s?1|\s?A\s?1|PRIO\s?1|^P\s?1"
     regex_prio2 = "^A\s?2|\s?A\s?2|PRIO\s?2|^P\s?2"
     regex_prio3 = "^B\s?1|^B\s?2|^B\s?3|PRIO\s?3|^P\s?3|PRIO\s?4|^P\s?4"
          
     def __init__(self, message, capcode, timestamp,flex):
         # init local variables
         self.message = message,
         self.capcode = capcode,
         self.timestamp = timestamp,
         self.flex = flex
         
         # filter prio out message with regex and set message color based on prio.
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
     
     # send or message to the connected websocket clients. 
     def sendToWebSocket(self):
         
        # create a json object
        jsonMessage = Object()
        jsonMessage.message = self.message[0]
        jsonMessage.timestamp = self.timestamp[0]
        jsonMessage.capcode = self.capcode[0]
        jsonMessage.prio =  self.prio.name

        # send json to all connected clients
        for client in server.connections.itervalues():
            if client != self:
                try:
                    client.sendMessage(jsonMessage.toJSON())
                except Exception as n:
                    print n

    # draw message to terminal screen
     def draw(self):
        print ' '
        print  colored(self.timestamp[0] ,'blue', attrs=['bold']), colored(self.message[0], self.color,  attrs=['bold']),
        print '                  ',
        print colored(self.capcode[0], 'white'),

# start the socket server
def start_server():  
    server.serveforever()
         
# create a thread to run socket server at the background. 
websocketThread = threading.Thread(target=start_server)
websocketThread.daemon = True
websocketThread.start()

try:
    # an endless loop to read alerts
    while True:
        # read line with mutigon this is the line printed when an alert was received
        line = multimon_ng.stdout.readline()
        
        # poll until an alert is reveived
        multimon_ng.poll()
        if line.__contains__("ALN"):
            if line.startswith('FLEX'):  
               # read group id from string it is at index 35-41
                groupid = line[35:41]

                # check if we received message before
                if groupid == groupidold: 
                    print colored(capcode, 'white'), 
                else:
                    # read flex, timestamp, capcode and message from line
                    flex = line[0:5]
                    timestamp = line[6:25]
                    capcode = line[43:52]
                    message = line[58:]
                    
                    # convert datetime to local datetime
                    utc = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
                    utc = utc.replace(tzinfo=tz.tzutc())
                    local = utc.astimezone(tz.tzlocal())
                    local = local.strftime("%d-%m-%Y %H:%M:%S")

                    # create message object with the valus read from line.
                    message = Message(message, capcode, local, flex)                       
                    message.draw()
                    message.sendToWebSocket()

                    # execute the alert script witch will make the leds on rpi blink
                    execfile('./Alarm.py')

                    # set or groupid to this new id so that we can know if message has already been received.
                    groupidold = groupid
                    
except KeyboardInterrupt:
    os.kill(multimon_ng.pid, 9)
