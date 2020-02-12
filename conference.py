
from entities import Entities

class  Conference(Entities):

    def __init__(self,data):
        Entities.__init__(self,data)
    
    """ representation  """ 
    def __repr__(self): 

        return "Conference: titre({}), resume({}),date({})".format(self.titre, self.resume,self.date)
