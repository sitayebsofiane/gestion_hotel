
from entities import Entities

class  Conference(Entities):

    def __init__(self,data):
        self.id_conference=None
        self.titre=None
        self.resume=None
        self.date=None
        Entities.__init__(self,data)
    
    """ representation  """ 
    def __repr__(self): 

        return "Conference: ID_confernce({}), titre({}), resume({}),date({})".format(self.id_conference,self.titre, self.resume,self.date)
