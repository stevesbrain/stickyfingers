# About StickyFingers
*StickyFingers* was born out of a need to insert the SHA256 fingerprints of Self-Signed SSL certs into ZNC 1.6 to be able to connect to certain networks.

There is obviously a relatively short process to do this using OpenSSL x509 tools, however, for IRC servers with a bunch of nodes as resolved by Round Robin DNS, it can get time consuming to dig + fetch certifiates + convert + fingerprint them.

This could relatively easily be circumvented with a shell script too, however, I wanted to practice my Python skills, and work on learning it a bit further, as well as making something a little nicer or more helpful than a shell script. Hence, *StickyFingers*
