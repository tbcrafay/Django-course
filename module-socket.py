import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/page.htm HTTP/1.1\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/page.htm HTTP/1.1\r\nHost: data.pr4e.org\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end='')

except socket.error as err:
    print(f"Error: {err}")

finally:
    mysock.close()
