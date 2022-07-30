import network
import time
import machine
import socket
import random
import urequests as requests
import ubinascii
import rp2

wlan = network.WLAN(network.AP_IF)
wlan.active(False)
wlan.config(essid='pico_w', channel=12, password = "123456789")


print("ssid", end="=")
print(wlan.config('ssid'))
print("chanel", end="=")
print(wlan.config('channel'))


wlan.active(True)
status = wlan.status('stations')
conn = wlan.isconnected()

def get_html(html_name):
    with open(index.html, 'r') as file:
        html = file.read()
        
    return html
# HTTP server with socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('Listening on', addr)
led = machine.Pin('LED', machine.Pin.OUT)
print(wlan.ifconfig())
# Listen for connections
while True: 
    try:
        time.sleep(35)
        print(status)
        cl, addr = s.accept()
        print('Client connected from', addr)
        r = cl.recv(1024)
        # print(r)
        
        r = str(r)
        led_on = r.find('?led=on')
        led_off = r.find('?led=off')
        print('led_on = ', led_on)
        print('led_off = ', led_off)
        if led_on > -1:
            print('LED ON')
            led.value(1)
            
        if led_off > -1:
            print('LED OFF')
            led.value(0)
            
        response = get_html('index.html')
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
        
    except OSError as e:
        cl.close()
        print('Connection closed')