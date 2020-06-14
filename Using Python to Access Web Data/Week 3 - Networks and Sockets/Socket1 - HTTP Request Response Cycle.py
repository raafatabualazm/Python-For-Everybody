import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
soc.send(cmd)

while True:
    data = soc.recv(5120)
    if len(data) < 1:
        break
    else:
        print(data.decode())

soc.close()