import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ('localhost', 55558)

fname = input("Enter File Name For transmission: ")
f = open(fname, "rb")
info = f.read(1024)

s.sendto(str.encode(fname, "utf-8"), addr)
# s.sendto(info, addr)

while info:
    if s.sendto(info, addr):
        info = f.read(1024)
        #print("sending file")
s.close()
f.close()
