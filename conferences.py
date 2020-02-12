import cgi
import cgitb
from model.model import Model
from view import View
cgitb.enable

form = cgi.FieldStorage()
model = Model("hotel","postgres","as122014","localhost","5432")
view = View(model)
# securisation
try:
    if form.getvalue("nom") and form.getvalue("pass"):
        nom=form.getvalue("nom")
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

html_body="""<body> <p>"""+view.display()+"""</p>"""+"""

"""

html_foot="""  <p>si voulez revenir a l'acueil cliquer <a href="index.py">ici</a></p>
</body> 
</html> """

print("Content-type: text/html; charset=utf-8")
print(html_head+html_body+html_foot)
