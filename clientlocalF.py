#!/usr/bin/env python
# coding: utf-8

import socket

#ip = "192.168.0.227" #ipRaspi
ip = "127.0.0.1"
port = 12500


trame = bytearray([51,8,30,45,30])
print "--Question-->"
print "Trame de Question :", str(trame).encode("hex")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(trame, (ip, port))


trame0, addr = sock.recvfrom(1024)

print "            "
print "<--Réponse--"
print "Trame de Réponse:",trame0.encode("hex")
print "ID=",ord(trame0[0])#affichage de l'octet 0
print "Lg=",ord(trame0[1])#affichage de l'octet 1
print "V.Vent=",ord(trame0[2])#affichage de l'octet 2
print "D.Vent=",ord(trame0[3])#affichage de l'octet 3
print "Gite=", ord(trame0[12])#affichage de l'octet 4
b3=ord(trame0[4])
b2=ord(trame0[5])
b1=ord(trame0[6])
b0=ord(trame0[7])

latitude=b3<<24|b2<<16|b1<<8|b0

if b3 > 127:
    latitude=(~latitude)&0XFFFFFFFF
    latitude=latitude+1
    latitude=latitude*-1

print "Latitude=",float(latitude)/10000000

b7=ord(trame0[8])
b6=ord(trame0[9])
b5=ord(trame0[10])
b4=ord(trame0[11])

longitude=b7<<24|b6<<16|b5<<8|b4

if b7 > 127:
    longitude=(~longitude)&0XFFFFFFFF
    longitude=longitude+1
    longitude=longitude*-1

print "Longitude=",float(longitude)/10000000
