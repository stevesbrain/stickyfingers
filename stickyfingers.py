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
        #Give us some initial values
        self.Host = HostName
        self.Port = PortNum
        #Connect to our target
        ConnectTarget = (self.Host, self.Port)
        #Get the certificate
        HostCert = ssl.get_server_certificate(ConnectTarget)
        #Convert into DER from PEM format
        lines = HostCert.replace(" ",'').split()
        der = a2b_base64(''.join(lines[1:-1]))
        #Get the SHA256 sum of the DER cert
        sha256.update(der)
        #Convert the sum into a printable format
        PrintableCert = sha256.hexdigest()
        #Iterate over it to convert to a nice printable format
        splitter = iter(PrintableCert)
        self.cert = FormattedCert = ':'.join(a+b for a,b in zip(splitter, splitter))

google = Get265("google.com", 443)

print(google.cert)
print(google.Host)
print(google.Port)
