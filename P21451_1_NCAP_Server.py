#Authors: Tom Morris, Keith Hall, Anas Muhamed, Tom Stodt, Jeff Welder
#Begin Date: 10.7.2014 Last Revision: 10.7.2014
#Description: This code runs an NCAP Server Module according to Proposed
#             Standard IEEE P21451-1

#-----------------------------INCLUDED LIBRARIES-------------------------
#loads socket commands for UDP Communication
import socket

#------------------------------GLOBAL VARIABLES--------------------------
#Defines IP addresses used in the Smart Sensor Network (Global Variables)
TOMM  = "192.168.1.200" #datatype string
ANAS  = "192.168.1.201" #datatype string
KEITH = "192.168.1.202" #datatpye string
JEFF  = "192.168.1.203" #datatype string
TOMS  = "192.168.1.204" #datatype string

#----------------------------Function Definitions------------------------

#Defines the main function for the SSN NCAP Server
#VOID Function
def NCAP_Server_Main():
    UDP_Send(ANAS, 5005, "TEST MESSAGE")
    print "SENT A TEST MESSAGE"
#end NCAP_Server_Main()

#Defines a universal message receive function to be used throughout NCAP
#Server
#receive_IP datatype is string
#listening_PORT datatype is integer
def UDP_Receive(receive_IP, listening_PORT):
    #creates a socket for receiving messages
    SOCKET_RECEIVE = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #listens on given port for a message
    SOCKET_RECEIVE.bind((receive_IP, listening_PORT))

    while True:
        data, addr = SOCKET_RECEIVE.recvfrom(1024)
        print "Received Message: ", data
#end UDP_Receive

#Defines a universal message sending function to be used throughout NCAP
#Server
#target_IP datatype is string
#target_PORT datatype is integer
#MESSAGE datatype is string
def UDP_Send(target_IP, target_PORT, MESSAGE):
    #creates a socket for sending the message
    SOCKET_SEND = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #sends the given message to the given target IP using the target port
    SOCKET_SEND.sendto(MESSAGE, (target_IP, target_PORT))
#end UDP_Send

#runs NCAP_Server_Main
NCAP_Server_Main()

