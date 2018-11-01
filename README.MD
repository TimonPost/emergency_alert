
This project was developed by KBS group 2 ICTM1S Windesheim year 1.

This is a project to read p2000 p2000 emergency alerts alerts. This could be done by plugging in a DVB-T usb receiver and installing the nessiarly drivers. 

This project contains the following files:

- index.html

  This is the web interface on witch incomming p2000 emergency alerts will be displayed.
- p2000.py

  Script to read p2000 emergency alerts from DVB-T usb. 
- SimpleWebsocketServer.py

  This script could be used setup a websocket for comunicating between python and the connected webbrouwsers.
- Mail.py 

  This is a script totaly not realated to this project but it could display incomming emails on a rasbarry pi sence had.

Realy what it is about is a website on witch the alerts will be displayed and a python script getting the data from the DBT-T usb. The data is send via a websocket to all connected clients (websites)
