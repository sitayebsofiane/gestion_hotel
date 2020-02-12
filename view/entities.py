
class Entities:

    def __init__(self,data):
        self.nom=None
        self.prenom=None
        self.description=None
        self.profession=None
        self.statut=None
        self.titre=None
        self.resume=None
        self.date=None
        self.hydrate(data)
    
    def hydrate(self, dicto):
        for key, value in dicto.items():
            if hasattr(self, key):
                setattr(self, key, value)
    
    
    