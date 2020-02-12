import http.server


port = 80
adress = ("",port)
server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories =["/"]
httpd = server(adress,handler)
print(f"Serveur demarré sur le port{port}")
#------------------------------------------------
#demarré le serveur en boucle
httpd.serve_forever()