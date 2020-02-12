
from entities import Entities

class  Speaker(Entities):

    def __init__(self,data):
        Entities.__init__(self,data)
    
    """ representation  """ 
    def __repr__(self): 

        return f"""Speaker: ID_speaker({self.id_speaker}),
        nom({self.nom}), prenom({self.prenom}),profession({self.profession}),statut({self.statut})"""
