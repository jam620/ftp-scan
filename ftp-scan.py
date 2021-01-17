
import socket

socket.setdefaulttimeout(2)

cliente=socket.socket()
cliente.connect(("morenojose.com",21))
respuesta = cliente.recv(1024)

print(respuesta)