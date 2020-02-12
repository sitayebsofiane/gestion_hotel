from view.speaker import Speaker
from view.conference import Conference


class View:
   

    def __init__(self,model):
        self.model=model

    def display(self):
        liste_of_dicto=self.model. get_all()
        liste_of_display=""
        
        print(" voici la liste des de tout coference anisi que  le nom des utilisateurs: ")
        for dicto in (liste_of_dicto):

            speaker = Speaker(dicto)
            conference = Conference(dicto)
            liste_of_display += "<p>"+(str(speaker)+" a animer "+str(conference))+"</p>"
        return liste_of_display
