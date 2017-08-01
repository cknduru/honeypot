from server import Server
from ftp_prot import FTP

server = Server()

ftp = FTP("FTP", 23)
    
if __name__ == "__main__":
    a = [ftp]
    server.createHoneypots(a)
