
from entities import Entities

class  Speaker(Entities):

    def __init__(self,data):
        Entities.__init__(self,data)
    
    """ representation  """ 
    def __repr__(self): 

        return "Speaker: ID_speaker({}),nom({}), prenom({})".format(self.id_speaker,self.nom, self.prenom)
