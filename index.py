#coding:utf-8
import cgi

print("Content-type: text/html; charset=utf-8\n")
var="str"
html="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    
    <title>Page test python html</title>
</head>
<body>
    <h1>hello tout le monde</h1>
    <p>si voulez gerer les conference taper <a href="conferences.py">ici</a></p>
    <p>si voulez gerer les conferencier taper <a href="speakers.py">ici</a></p>
    
</body>
</html>

"""
print(html)