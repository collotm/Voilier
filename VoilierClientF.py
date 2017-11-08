#!/usr/bin/env python
# coding: utf-8

import socket

class VoilierClient:

        def __init__(self):
                self.id_trame=0;
                self.ipserveur=""
                self.portserveur=0
                self.valeurSafran=0
                self.valeurGV=0
                self.gite=0
                self.lattitude=0
                self.longitude=0
                self.vitessevent=0
                self.orientationvent=0

        def initCom(self,ipserveur,portserveur):
                self.ipserveur=ipserveur
                self.portserveur=portserveur
                self.sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

        def txrx(self):
                trame = bytearray([self.id_trame,2,self.valeurSafran,self.valeurGV])
                print "--Question-->"
                print "trame Question :", str(trame).encode("hex")
                self.sock.sendto(trame, (self.ipserveur, self.portserveur))
                tramereponse, addr = self.sock.recvfrom(1024)


                b3=ord(tramereponse[4])
                b2=ord(tramereponse[5])
                b1=ord(tramereponse[6])
                b0=ord(tramereponse[7])

                lattitude=b3<<24|b2<<16|b1<<8|b0

                if b3 > 127:
                        lattitude=(~lattitude)&0XFFFFFFFF
                        lattitude=lattitude+1
                        lattitude=lattitude*-1


                b7=ord(tramereponse[8])
                b6=ord(tramereponse[9])
                b5=ord(tramereponse[10])
                b4=ord(tramereponse[11])

                longitude=b7<<24|b6<<16|b5<<8|b4

                if b7 > 127:
                        longitude=(~longitude)&0XFFFFFFFF
                        longitude=longitude+1
                        longitude=longitude*-1


                self.gite= ord(tramereponse[12])
                self.vitessevent=ord(tramereponse[2])
                self.orientationvent=ord(tramereponse[3])
                self.lattitude=float(lattitude)/10000000
                self.longitude=float(longitude)/10000000


        

monVoilierClient=VoilierClient()
monVoilierClient.initCom("127.0.0.1",12500)
monVoilierClient.valeurSafran=18;
monVoilierClient.valeurGV=65;
monVoilierClient.txrx()
print monVoilierClient.lattitude
print monVoilierClient.longitude
print monVoilierClient.gite



