from protocol import Protocol

class FTP(Protocol):
    def __init__(self, name, port):
        Protocol.__init__(self, name, port)

    def register(self, data):
        #print "{0} reporting in on port {1}!".format(self.name, self.port)
        print "got {0}".format(data)
    
#ftp = FTP("ftp")
#ftp.register()  
