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
    <form action="result.py" method="POST">
        <p><label id="nom">taper votre nom:</label>
        <input type="text" placeholder="taper votre nom" id="nom" name="nom"/></p>
        <p><label id="pass">taper votre nom:</label>
        <input type="password"  id="pass" name="pass"/></p>
        <p><input type="submit" value="Envoyer"></p>

    </form>
</body>
</html>

"""
print(html)