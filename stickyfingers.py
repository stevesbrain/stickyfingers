#Import some libs and stuff
import ssl
import hashlib
#from socket import socket

sha256 = hashlib.sha256()

#s = socket()
#Define our host and port
#TODO we'll be calling this via command line
Host = ('host', 6697)
HostCert = ssl.get_server_certificate(Host).encode('utf-8')
sha256.update(HostCert)
PrintableCert = sha256.hexdigest()
print(PrintableCert)
