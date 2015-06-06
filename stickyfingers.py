#Import some libs and stuff
import ssl
import hashlib
from binascii import a2b_base64


#Set the scene for our hashes
sha256 = hashlib.sha256()

#Define our host and port
#TODO we'll be calling this via command line
Host = ('hosthosthosthosthost', 6697)
#Grab the certificate and encode in utf-8
HostCert = ssl.get_server_certificate(Host)  #.encode('utf-8')
#Convert from PEM to DER
lines = HostCert.replace(" ",'').split()
der = a2b_base64(''.join(lines[1:-1]))
#Checksum the certificate
sha256.update(der)
#Make it nice and printable, then show it
PrintableCert = sha256.hexdigest()
print(PrintableCert)
