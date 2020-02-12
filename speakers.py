import cgi
import cgitb
from model.model import Model
from view import View
cgitb.enable

form = cgi.FieldStorage()
model = Model("hotel","postgres","as122014","localhost","5432")
view = View(model)

if form.getvalue("nom") and form.getvalue("prenom") and form.getvalue("desc") and form.getvalue("profession"):
    nom = form.getvalue("nom")
    prenom = form.getvalue("prenom")
    desc = form.getvalue("desc")
    profession = form.getvalue("profession")
    model.insert_speaker(nom,prenom,desc,profession)
if form.getvalue("id_speaker"):
    id_speaker = form.getvalue("id_speaker")
    model.delete_speaker(id_speaker)

html_head="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style> 
            p{
            background-color:rgb(8, 184, 52);;
                }
    </style>
    <title>Page test python html</title>
</head>
"""

html_body=""" <body> <p>"""+view.display_speakers()+"""</p>"""+"""
<form method="post">
 
        <fieldset>
            <legend>Ajouter un conferencier</legend> 
     
            <label for="nom">Quel est le nom du conferencier ?</label>
            <input type="text" name="nom" id="nom" />
      
            <label for="prenom">le prenom du conferencier ?</label>
            <input type="text" name="prenom" id="prenom" />

            <label for="desc">description ?</label>
            <input type="text" name="desc" id="desc" />

            <label for="profession">profession ?</label>
            <input type="text" name="profession" id="profession" />
        </fieldset>
        <fieldset>
            <legend>suprimer un conferencier</legend> 
            <label for="id_speaker">Quel est l'id du conferencier que tu veut suprimer</label>
            <input type="number" name="id_speaker" id="id_speaker" />
        </fieldset>
        <input type="submit" value="Envoyer" />
   </form>
"""

html_foot="""  <h2>si voulez retourner a l'acueil clique <a href="index.py">ici</a></h2>
                </body> 
                </html> """

print("Content-type: text/html; charset=utf-8")
print(html_head+html_body+html_foot)
