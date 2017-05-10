
import random 


class Card():
    
    def __init__(self, Rank, Suit):
        self.rank = Rank
        self.suit = Suit
        
    def __str__(self):  
        return str(self.rank)+str(self.suit)
        
    def Point(self):
        numList = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
        JQK = ["J", "Q", "K"]
        if str(self.rank) in numList:
            point = int(self.rank)
        elif str(self.rank) in JQK:
            point = 10
        elif str(self.rank) == "A":
            point = 11
        return point
  
  
  
        
        
class Deck():
    
    def __init__(self):
        RankList = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        SuitList = ["C", "D", "H", "S"]
        
        #loop to create the card list
        self.cardList = []
        for i in range(4):
            in_suit = SuitList[i]
            for j in range(13):
                in_rank = RankList[j]
                new_Card = Card(in_rank, in_suit)
                self.cardList.append(new_Card)
               
            
    def __str__(self):
        
        #cardobject has different len, this is use to format them properly 
        if len(str(self.cardList[0])) == 3:
            string = " "
        if len(str(self.cardList[0])) == 2:
            string = "  "
        
        #loop through the card list to create a string
        for i in range(0,len(self.cardList)):
                if i%13 == 0 and i != 0:
                    if len(str(self.cardList[i])) == 3 : 
                        string += "\n "
                    elif len(str(self.cardList[i])) == 2:
                        string += "\n  "
                elif i%13 != 0  and len(str(self.cardList[i])) == 2:
                    string += "  "
                elif i%13 != 0  and len(str(self.cardList[i])) == 3:
                    string += " "
    
                string += str(self.cardList[i])
                
        return string
        
    def shuffle(self):
        random.shuffle(self.cardList)
    
    def dealOne(self, user):
        card = self.cardList[0]
        user.hand.append(card)
        user.handTotal += card.Point()
        del self.cardList[0]
        
        
        
        
    
class Player():
    
    def __init__(self):
        self.hand = []
        self.handTotal = 0
        
    def __str__(self):
        out = " "
        for item in self.hand:
            out += (str(item) + "  ")
        return out
      
    
    
    
def showHands(opponent,dealer):
    print ("Dealer shows", dealer.hand[1] , "faceup")
    print ("You show", opponent.hand[1] , "faceup")
    


def opponentTurn(cardDeck,dealer,opponent):
    print ()
    print ("You go first.")
    print ()
    
    
    Alist = ["AH", "AC", "AD", "AS" ]
    switch = 0    
    if str(opponent.hand[0]) in Alist:
        switch += 1
    if str(opponent.hand[1]) in Alist:
        switch += 1
    
    #check if player has A card, and how many they have 
    #give player a choice when have two As at the begining
    if str(opponent.hand[0]) in Alist and str(opponent.hand[1]) in Alist:
        print ("Holding two aces will be over 21!")
        choice_A = eval(input("Choose 1 to switch one ace to 1 point or to switch both aces to 1 point: "))
        print()
        if choice_A == 1:
            print ("Switching one ace to 1 point!")
            opponent.handTotal -= 10
            switch -= 1
        elif choice_A == 2:
            print ("Switching both aces to 1 point!")
            opponent.handTotal -= 20
            switch -= 2
    elif str(opponent.hand[0]) in Alist or str(opponent.hand[1]) in Alist:
        print ("Assuming 11 points for an ace you were dealt for now.")
        
    
    while 21 >= opponent.handTotal :
            
        print("You hold "+ str(opponent) + "for a total of", opponent.handTotal)
        choice = eval(input("1 (hit) or 2 (stay)? "))
        
        
        if choice == 1:
            Deck.dealOne(cardDeck, opponent) 
            print()
            print ("Card dealt: " , opponent.hand[-1])
            if str(opponent.hand[-1]) in Alist:
                switch += 1 
            
            if opponent.handTotal == 21:
                print ("21!  My turn. . .")
                break
                
            elif (opponent.handTotal > 21) and switch >= 1 :
                print ("Over 21.  switching an ace from 11 points to 1.")
                opponent.handTotal -= 10
                print ("New total: ", opponent.handTotal)
                print ()
                switch -= 1
                
            elif (opponent.handTotal > 21):
                print ("You has", opponent.handTotal, "You busts!  Dealer win.") 
                print ()  
                break 
            
        elif choice == 2:
            print ("Staying with ", opponent.handTotal)
            print ()
            break
            
        else:
            print ("Invalid input, please re-enter!")
            choice = eval(input("1 (hit) or 2 (stay)? 1 "))
        
        
   
def dealerTurn(cardDeck,dealer,opponent):
    
    if opponent.handTotal > 21:
        print ("Clearly, the Winning is belong to Dealer!")
        print ()
        
    else:
        print ("Dealer's turn")
        print ("Your hand: "+ str(opponent) + "  for a total of", opponent.handTotal)
        print ("Dealer's hand: " + str(dealer) +"  for a total of", dealer.handTotal )
        print ()
        
        
        Alist = ["AH", "AC", "AD", "AS" ]
        switch = 0    
        if str(dealer.hand[0]) in Alist:
            switch += 1
        if str(dealer.hand[1]) in Alist:
            switch += 1
        #check if player has A card
        
        if str(dealer.hand[0]) in Alist and str(dealer.hand[1]) in Alist:
            print ("Dealer has two Aces!")
            print ("Assuming 11 points for one ace, and switch another ace to 1 point!") 
            print ()
            dealer.handTotal -= 10
            switch -= 1
        elif str(dealer.hand[0]) in Alist or str(dealer.hand[1]) in Alist:
            print ("Assuming 11 points for an ace Dealer was dealt for now.")
        
            
        if dealer.handTotal >= opponent.handTotal:
            print ("Dealer has %d.  Dealer wins! You lose..."%(dealer.handTotal))
            print()
            
        else:
            
            while dealer.handTotal < 21:
                Deck.dealOne(cardDeck, dealer)  
                print ("Dealer hits: ", dealer.hand[-1])
                print ("New total:", dealer.handTotal)
                print ()
        
                if str(dealer.hand[-1]) in Alist:
                    switch += 1

                if dealer.handTotal == 21:
                    print ("Dealer has 21. Dealer wins! You lose")
                    print () 
                    break
                elif dealer.handTotal > 21 and switch >= 1 :
                    print ("Over 21.  switching an ace from 11 points to 1.")
                    dealer.handTotal -= 10
                    print ("New total: ", dealer.handTotal)
                    print ()
                    switch -= 1
                elif dealer.handTotal > 21:
                    print ("Dealer has %d.  Dealer busts!  You win." %(dealer.handTotal))
                    print ()    
                elif dealer.handTotal >= opponent.handTotal:
                    print ("Dealer has %d.  Dealer wins! You lose..."%(dealer.handTotal))
                    print () 
                    break
            
        
        
        
        
def main():

    cardDeck = Deck()               # create a deck of 52 cards called "cardDeck"
    print ("Initial deck:")
    print(cardDeck)                 # print the deck so we can see that you built it correctly
    print ()

    random.seed(50)                 # leave this in for grading purposes
    cardDeck.shuffle()              # shuffle the deck
    print("Shuffled deck")
    print(cardDeck)                 # print the deck so we can see that your shuffle worked
    print ()
    
    dealer = Player()               # create the player:  you play for this Player
    opponent = Player()             # create the dealer:  the computer plays for this Player
    
    cardDeck.dealOne(opponent)      # face up
    cardDeck.dealOne(dealer)        # face down (the "hole" card)
    cardDeck.dealOne(opponent)      # face up
    cardDeck.dealOne(dealer)        # face up

    print ("Deck after dealing two cards each:")
    print (cardDeck)
    print ()
    print ()
    print () 
    
    showHands(opponent,dealer)      # remember not to show face down cards
    

    opponentTurn(cardDeck,dealer,opponent)     # this is where half of the hard stuff is done
    dealerTurn(cardDeck,dealer,opponent)       # this is where the other half of the hard stuff is done
    
    print ("Game over.")
    print ("Final hands:")
    print ("   Dealer:   ", dealer)
    print ("   Opponent: ", opponent)
    
main()

