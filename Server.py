import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 55558))

data, addr = s.recvfrom(1024)
print("Recieved File:", data.decode(), data.strip())
f = open('file_'+data.decode(), 'wb')

data, addr = s.recvfrom(1024)
try:
    while data:
        f.write(data)
        s.settimeout(2)
        data, addr = s.recvfrom(1024)
except socket.timeout:
    f.close()
    s.close()
    print("file recieved")
