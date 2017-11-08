#!/usr/bin/env python
# coding: utf-8

import socket

idTrame=51
lg=8
vitVent = 30
dirVent = 45
gite = 30
 
#ip = "192.168.0.227" #ipRaspi
ip = "127.0.0.1"
port = 12500

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip, port))

latitude=-16511782
b3=(latitude>>24)&0xFF
b2=(latitude>>16)&0xFF
b1=(latitude>>8)&0xFF
b0=latitude&0xFF

longitude=-56988541
b7=(longitude>>24)&0xFF
b6=(longitude>>16)&0xFF
b5=(longitude>>8)&0xFF
b4=longitude&0xFF

while True:
    data, addr = sock.recvfrom(5)

    print "--Question-->"
    print "UDP Target IP :", ip
    print "UDP Target Port :", port
    print "ID=",ord(data[0])
    print "Lg=",ord(data[1])
    print "GV=",ord(data[2])
    print "Sf=",ord(data[3])
    

    trame1 = bytearray([idTrame,lg,vitVent,dirVent,b3,b2,b1,b0,b7,b6,b5,b4,gite])
    
    print "            "
    print "<--Réponse--"
    print "Trame de Réponse :" , str(trame1).encode("hex")

    sock.sendto(trame1,addr)
