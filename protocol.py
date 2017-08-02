class Protocol(object):
    def __init__(self, name, port):
        self.name = name
        self.port = port

    def register(self):
        raise NotImplementedError("register() must be implemented")
    
    #def __str__(self):
        #return "{0}->{1}".format(self.name, self.port)
        pass
