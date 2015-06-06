import ssl
from socket import socket

s = socket()
host = ('host', 6697)
c = ssl.get_server_certificate(host)
print(c)