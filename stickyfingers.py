#Import some libs and stuff
import ssl
import hashlib
from binascii import a2b_base64


#Set the scene for our hashes
sha256 = hashlib.sha256()


class Get265:
    """Takes the hostname/IP address
    and relevant port numbers, and returns a beautiful
    SHA256 fingerprint of the cert; in this case,
    specifically for use with ZNC 1.6"""
    def __init__(self, HostName, PortNum):
        Host = HostName
        Port = PortNum
        ConnectTarget = (Host, Port)
        HostCert = ssl.get_server_certificate(ConnectTarget)
        lines = HostCert.replace(" ",'').split()
        der = a2b_base64(''.join(lines[1:-1]))        
        sha256.update(der)
        PrintableCert = sha256.hexdigest()
        splitter = iter(PrintableCert)
        self.cert = FormattedCert = ':'.join(a+b for a,b in zip(splitter, splitter))        
        
#Define our host and port
#TODO we'll be calling this via command line
#Host = ('hosthosthosthosthost', 6697)
#Grab the certificate and encode in utf-8
#HostCert = ssl.get_server_certificate(Host)  #.encode('utf-8')
#Convert from PEM to DER
#lines = HostCert.replace(" ",'').split()
#der = a2b_base64(''.join(lines[1:-1]))
#Update checksum with the certificate
#sha256.update(der)
#Make it nice and printable, with semicolons between every second character
#PrintableCert = sha256.hexdigest()
#splitter = iter(PrintableCert)
#FormattedCert = ':'.join(a+b for a,b in zip(splitter, splitter))
google = Get265("google.com", 443)
print(google.cert)
