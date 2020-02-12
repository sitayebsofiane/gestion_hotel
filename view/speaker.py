
from view.entities import Entities

class  Speaker(Entities):

    def __init__(self,data):
        Entities.__init__(self,data)
    
    """ representation  """ 
    def __repr__(self): 

        return "Speaker: nom({}), prenom({})".format(self.nom, self.prenom)
