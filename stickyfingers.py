#Import some libs and stuff
import hashlib, ssl, argparse
from binascii import a2b_base64

parser = argparse.ArgumentParser()
parser.add_argument("-hn", "--hostname", dest="hostname", help="Hostname", type=str)
parser.add_argument("-p", "--port", dest="port", help="Port number", type=int)

args = parser.parse_args()

class CheckSum:
    """Takes the hostname/IP address \
    and relevant port numbers, and returns a beautiful \
    SHA256 fingerprint of the cert; in this case, \
    specifically for use with ZNC 1.6"""
    def __init__(self, HostName, PortNum):
        """Initial action performed on the classi \
        to fetch the SSL certificate, and convert to DER"""
        #Give us some initial values
        self.HostName = HostName
        self.PortNum = PortNum
        ConnectTarget = (self.HostName, self.PortNum)
        #Get the certificate
        HostCert = ssl.get_server_certificate(ConnectTarget)
        #Convert into DER from PEM format
        lines = HostCert.replace(" ",'').split()
        self.der = der = a2b_base64(''.join(lines[1:-1]))
    def formatString(self, cert):
        """Formats whatever string you throw at it \
        in XX:XX:XX format. The Certificate is thrown \
        as the variable here."""
        self.cert = cert
        splitter = iter(cert)
        certFormat = ':'.join(a+b for a,b in zip(splitter, splitter))
        return(certFormat)
    def Get256(self):
        """Returns the SHA256 fingerprint of the DER cert"""
        sha256 = hashlib.sha256()
        #Get the SHA256 sum of the DER cert
        sha256.update(self.der)
        #Convert the sum into a printable format
        PrintableCert = sha256.hexdigest()
        returnCert = self.formatString(PrintableCert)
        print("SHA256 fingerprint:", returnCert)
    def Get1(self):
        """Returns the SHA1 fingerprint of the DER cert"""
        sha1 = hashlib.sha1()
        sha1.update(self.der)
        PrintableCert = sha1.hexdigest()
        returnCert = self.formatString(PrintableCert)
        print("SHA1 fingerprint:", returnCert)
value = CheckSum(args.hostname, args.port)
value.Get256()