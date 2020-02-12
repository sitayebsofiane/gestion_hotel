import cgi
import cgitb

cgitb.enable

form = cgi.FieldStorage()

# securisation
try:
    if form.getvalue("nom") and form.getvalue("pass"):
        nom=form.getvalue("nom")
        display=f"<h1> bonjour: {nom}</h1> "
    else:
        raise Exception("<h1> erreur</h1> ")
except:
    display="<h1> erreur</h1> "
html_head="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    
    <title>Page test python html</title>
</head>
"""

html_body="""
<body>
"""

html_foot="""
</body>
</html>
"""
print("Content-type: text/html; charset=utf-8\n")
print(html_head+html_body+display+html_foot)
