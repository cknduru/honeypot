from server import Server
from ftp_prot import FTP

server = Server()

ftp = FTP("FTP", 10009)
smtp = FTP("SMTP", 6007)
    
if __name__ == "__main__":
    a = [ftp, smtp]
    server.createHoneypots(a)
