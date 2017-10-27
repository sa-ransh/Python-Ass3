
from card import Card
from random import seed,randint

class Deck:

    def __init__(self, valueStart, valueEnd, numSuits):
        self.pile = []
        self.size = 0

        values = []

        i = valueStart

        while i <= valueEnd:
            values.append(i)
            i += 1

        i = 0

        while i < numSuits:
            for value in values:
                newCard = Card(value,i)
                self.pile.append(newCard)
                self.size += 1
            i += 1

    def __str__(self):
        newString = ""

        for card in self.pile:
            newString += (str(card) + ',')

        newString = newString[:-1]

        return newString

    def __len__(self):
        return self.size

    #adds an item at location where
    def addCard(self, card, where):
        if where > -1 and where <= self.size:
            self.pile = self.pile[:where] + [card] + self.pile[where:]
            self.size += 1
        else:
            print("I can't add there.")

    #draw a card from the top of the deck
    def drawCard(self):
        item = self.pile.pop()
        self.size -= 1

        return item

    def placeCardTop(self, card):
        self.addCard(card, self.size)

    def placeCardBottom(self,card):
        self.addCard(card, 0)

    def shuffle(self,**kwargs):

        newPile = []

        if "seed" in kwargs:
            seed(kwargs["seed"])

        while len(self.pile) > 0:
            item = randint(0, len(self.pile)-1)

            newPile.append(self.pile[item])

            del(self.pile[item])

        self.pile = newPile


def main():
    new_deck = Deck(1, 5, 5)
    print(new_deck)
    testCard = Card(6,6)

    new_deck.placeCardTop(testCard)
    new_deck.placeCardBottom(testCard)

    print(new_deck)

    new_deck.shuffle()

    print(new_deck)

if __name__ == "__main__":
    main()