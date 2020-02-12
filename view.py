from speaker import Speaker
from conference import Conference


class View:
   

    def __init__(self,model):
        self.model=model
    """ display speakers and conferences """
    def display(self):
        liste_of_dicto=self.model.get_all()
        str_of_display=""
        
        for dicto in (liste_of_dicto):

            speaker = Speaker(dicto)
            conference = Conference(dicto)
            str_of_display += "<p>"+(str(speaker)+" a animer "+str(conference))+"</p>"
        return str_of_display
    
    """ display speakers """
    def display_speakers(self):
        liste_of_dicto=self.model.get_all_speakers()
        str_of_display=""
        
        for dicto in (liste_of_dicto):
            if dicto["statut"]:
                speaker = Speaker(dicto)
                str_of_display += "<p>" + str(speaker)  + "</p>"
        return str_of_display
    
    

