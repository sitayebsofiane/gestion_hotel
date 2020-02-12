import cgi
import cgitb
from model.model import Model
from view import View
cgitb.enable

form = cgi.FieldStorage()
model = Model("hotel","postgres","as122014","localhost","5432")
view = View(model)
if form.getvalue("titre") and form.getvalue("resume") and form.getvalue("date") and form.getvalue("id_speaker"):
    titre = form.getvalue("titre")
    resume = form.getvalue("resume")
    date = form.getvalue("date")
    id_speaker = form.getvalue("id_speaker")
    model.insert_conf(titre,resume,date,id_speaker)
    
html_head="""
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
"""

html_body="""<body> 
<p>"""+view.display()+"""</p>"""+"""
 <form method="post">
 
        <fieldset>
            <legend>Ajouter une conference</legend> <!-- Titre du fieldset --> 
     
            <label for="titre">Quel est le titre de la conference ?</label>
            <input type="text" name="titre" id="titre" />
     
            <label for="resume">Quel est le resumer ?</label>
            <input type="text" name="resume" id="resume" />
      
            <label for="date">la date ?</label>
            <input type="date" name="date" id="date" />

            <label for="id_speaker">id_speaker ?</label>
            <input type="number" name="id_speaker" id="id_speaker" />
        </fieldset>
        <fieldset>
            <legend>suprimer une conference</legend> <!-- Titre du fieldset --> 
     
            <label for="id_conf">Quel est l'id de la conference que tu veut suprimer</label>
            <input type="number" name="id_conf" id="id_conf" />
        </fieldset>
   </form>
"""

html_foot="""  <h2>si voulez revenir a l'acueil cliquer <a href="index.py">ici</a></h2>
</body> 
</html> """

print("Content-type: text/html; charset=utf-8")
print(html_head+html_body+html_foot)
