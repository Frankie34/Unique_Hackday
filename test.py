import optparse
from socket import *
from threading import *

screenLock = Semaphore(value=1)

def connScan(tgtHost,tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        connSKt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        screenLock.acquire()
        print'[+] %d/tcp open' % tgtPort
        print'[+] ' + str(results)
        #connSkt.close()
    except:
        screenLock.acquire()
        print '[-] %d/tcp closed' % tgtPort
    finally:
        screenLock.release()
        connSkt.close()        

def portScan(tgtHost,tgtPorts):
     try:
         tgtIP = gethostbyname(tgtHost)
     except:
         print "[-] Cannot resolve '%s': Unknown host"%tgtHost
         return
     try:
         tgtname = gethostbyaddr(tgtIP)
         print '\n[+] Scan Results for: ' +tgtname[0]
     except:
         print '\n[+] Scan Results for: ' +tgtIP
     
     setdefaulttimeout(1)
     for tgtPort in tgtPorts:
        t = Thread(target=connScan,args=(tgtHost,int(tgtPort)))
        t.start()

def main():
    parser = optparse.OptionParser("usage %prog "+\
        "-H <target host> -p <target port>")
    parser.add_option('-H', dest = 'tgtHost', type = 'string', \
        help = 'specify target host')
    parser.add_option('-p', dest = 'tgtPort', type = 'string', \
        help = 'specify target port[s] seperate by comma')
    
    (options, args) = parser.parse_args()
    
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    
    if(tgtHost == None) | (tgtPorts[0] == None):
            print '[-] You must specify a target host and port[s].'
            exit(0)
    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
        main()


















