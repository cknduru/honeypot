import SocketServer
import thread
from threading import Thread, Lock
from ftp_prot import FTP

m = Lock()
ftp = FTP("FTP")

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data

        #echo data back
        self.request.sendall(self.data)


class Server():
    def __init__(self):
        pass
        
    def spawn_server(self, port):
            m.acquire()
            print 'Spawning honey pot on port', port
            SocketServer.TCPServer.allow_reuse_address = True
            server = SocketServer.TCPServer(("", port), MyTCPHandler)
            m.release()
            server.serve_forever()
                   
    def createHoneypots(self, honey_list):
        for pot in honey_list:
            #Thread(target = spawn_server, args = (port,)).start()
            pot.register()
    
if __name__ == "__main__":
    pass
