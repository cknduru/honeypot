from protocol import Protocol

class FTP(Protocol):
    def __init__(self, name):
        Protocol.__init__(self, name)

    def register(self):
        print "{0} reporting in!".format(self.name)
    
#ftp = FTP("ftp")
#ftp.register()  
