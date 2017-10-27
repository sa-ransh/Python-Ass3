class Card:

    def __init__(self,faceValue,suitType):
        self.face = faceValue
        self.suit = suitType

    def getFace(self):
        return self.face

    def getSuit(self):
        return self.suit

    def __str__(self):
        return str(self.getFace()) + ":" + str(self.getSuit())
