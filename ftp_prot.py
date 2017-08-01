from protocol import Protocol

class FTP(Protocol):
    def __init__(self, name, port):
        Protocol.__init__(self, name, port)

    def register(self):
        print "{0} reporting in on port {1}!".format(self.name, self.port)
    
#ftp = FTP("ftp")
#ftp.register()  
