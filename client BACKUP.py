#!/usr/bin/env python
# coding: utf-8

import socket

ip = "192.168.0.227" #remplacer par l'ip
port = 12500
msg = "Hello, World"

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)
sock.sendto(msg, (ip, port))
