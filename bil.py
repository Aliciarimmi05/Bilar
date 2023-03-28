#skapade en klass

class Bil:

    #construktor
    def __init__(self, fabrikat, colour, lager ):
        
        self.fabrikat=fabrikat
        self.colour =colour
        self.lager =lager

    def setFabrikat(self,fabrikat):
        self.fabrikat=fabrikat

    def getFabrikat(self):
        return self.fabrikat
    
    def setColour(self, colour):
        self.colour = colour

    def getColour(self):
        return self.colour