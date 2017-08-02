import SocketServer
import thread
from threading import Thread, Lock
from ftp_prot import FTP

m = Lock()
methods = {}

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
    	print "connection from {0}".format(self)
        server_addr = self.server.server_address[1]
        
        self.data = self.request.recv(1024).strip()
        methods[server_addr].register(self.data)

        #echo data back
        self.request.sendall(self.data)

class Server():
    def __init__(self):
        pass
        
    def spawn_server(self, pot):
            m.acquire()
            print 'Spawning honey pot on port', pot.port
            SocketServer.TCPServer.allow_reuse_address = True
            server = SocketServer.TCPServer(("", pot.port), MyTCPHandler)
            methods[pot.port] = pot # register method pointer at service name index

            print "registered protocol @ {0}".format(methods[pot.port])
            m.release()
            server.serve_forever()
                   
    def createHoneypots(self, honey_list):
        for pot in honey_list:
            Thread(target = self.spawn_server, args = (pot,)).start()
    
if __name__ == "__main__":
    pass
