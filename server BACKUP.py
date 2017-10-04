#!/usr/bin/env python
# coding: utf-8

import socket

ip = "192.168.0.227"
port = 12500

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print 'Demarrage ..'
sock.bind((ip, port))

while True:
    data, addr = sock.recvfrom(5)
    print data
