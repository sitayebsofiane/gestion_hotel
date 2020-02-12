#coding:utf-8
import cgi

print("Content-type: text/html; charset=utf-8\n")
var="str"
html="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style> 
            p{
            background-color: rgb(8, 184, 52);;
                }
    </style>
    <title>Page test python html</title>
</head>
<body>
    <h1>hello tout le monde</h1>
    <h2>si voulez gerer les conference taper <a href="conferences.py">ici</a></h2>
    <h2>si voulez gerer les conferencier taper <a href="speakers.py">ici</a><h2p>
    
</body>
</html>

"""
print(html)