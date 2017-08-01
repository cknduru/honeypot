class Protocol(object):
    def __init__(self, name):
        self.name = name

    def register(self):
        raise NotImplementedError("register() must be implemented")
    
    def __str__(self):
        return "protocol name: {0}".format(self.name)
