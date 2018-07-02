from __future__ import print_function
from websocket_server import WebsocketServer
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative
from rasp_on_drone import open_dump
import sys
import getopt


# Called for every client connecting (after handshake)
def new_client(client, server):
	print("New client connected and was given id %d" % client['id'])
	server.send_message_to_all("Hey all, a new client has joined us")


# Called for every client disconnecting
def client_left(client, server):
	print("Client(%d) disconnected" % client['id'])

# Called when a client sends a message
def message_received(client, server, message):
	if len(message) > 200:
		message = message[:200]+'..'
	print("Client(%d) said: %s" % (client['id'], message))
	server.send_message(client, "nihao")
        print("call_drone")
        from drone_ import call_drone, back_drone
	call_drone()
        print("do_by_ras")
	open_dump()
        print("back_drone")
	back_drone()


opts, args = getopt.getopt(sys.argv[1:], "h:p:", ["help"])
ip = ""
port = ""
for op, value in opts:
    if op == "-h":
        ip = value
    elif op == "-p":
        port = value
    else :
        print("Usage: python server.py -h <ip> -p <port>")
        sys.exit()

PORT=port
server = WebsocketServer(PORT, host=ip)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()
