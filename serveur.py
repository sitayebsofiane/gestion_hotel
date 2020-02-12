import http.server
import socketserver

port = 80
adress = ("",port)
handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(adress,handler)
print(f"serveur demarré sur le port {port}")
#------------------------------------------------
#demarré le serveur en boucle
httpd.serve_forever()