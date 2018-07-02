import websocket
import temperature
import mail
import ConfigParser
import sys
import getopt

def usage():
    print "Usage: python send_temperature_to_drone.py  -h <host> -p <port>"

if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "h:p:", ["help"])
    ip = ""
    port = ""
    for op, value in opts:
        if op == "-h":
            ip = value
        elif op == "-p":
            port = value
        else :
            usage()
            sys.exit()

    ws = websocket.WebSocket()
    ws.connect("ws://" + ip + ":" + port)

    cf = ConfigParser.ConfigParser()
    cf.read("config.private")
    threshold = cf.getint("alert", "threshold")
    #eml = mail.Mail()
    temp = temperature.Temperature()
    while True:
        flag, t, h = temp.check()
        if flag and  t >= threshold:
            ws.send(str(t))
            #eml.sendEmail(t)
 
