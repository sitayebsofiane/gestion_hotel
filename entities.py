
class Entities:

    def __init__(self,data):
        
        self.hydrate(data)
    
    def hydrate(self, dicto):
        for key, value in dicto.items():
            if hasattr(self, key):
                setattr(self, key, value)
    
    
    