import random
from textwrap import dedent
from sys import exit

class Cards:

    #Creates the deck object for the other classes to use
    def __init__(self):
        self.deck = Cards.class_deck

    #Create the deck, disregarding suits, then shuffle it
    cards = []
    card_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    for i in range(4):
        for num in card_nums:
            cards.append(num)
    random.shuffle(cards)

    #Convert integer strings to integers
    class_deck = []
    for num in cards:
        try:
            num.isdigit()
            if num.isdigit() == True:
                num = int(num)
                class_deck.append(num)
            else:
                class_deck.append(num)
        except Exception:
            'Error with the try loop in class Cards'


class Game:
    #pulls the deck object into this class (composition).
    #This class has-a deck object
    def __init__(self, deck):
        self.deck = deck.class_deck
        self.dealer = []
        self.player = []

    #intro the game to help players who have never played blackjack.
    #Also explains why some blackjack rules are missing
    def play(self):
        print(dedent("""
        Hello and welcome to BlackJack! The rules are simple: be closer to
        21 than the dealer without going over. Face cards are worth 10. Aces
        can be worth 1 or 11, depending on which value benefits the player more.

        In traditional blackjack you can "split", "double", and "surrender".
        You can do none of those in this version because I didn't feel like
        coding them in. Also, there are no suits present because hearts are
        just as valuable as diamonds according to The Eagles, and also because
        I didn't feel like coding those in either. Just be aware that there are
        four sets of Kings(K), Queens(Q), etc. in the game.
        Roll Tide!

        Coded by Matt M.
        """))
        Game.draw_dealer(self)

    #function for dealing opening cards to the dealer
    def draw_dealer(self):

        print("Length of deck at start of game", len(self.deck))
        print("=="*20)
        print("Let's start the game")
        print("=="*20, "\n")

        self.dealer.append(self.deck.pop())
        self.dealer.append(self.deck.pop())

        print(dedent(f"""
        The dealer draws two cards first, revealing one to the player.
        The dealer's card is:
        {self.dealer[-1]}"""))
        Game.draw_player(self)

    #function for drawing and playing the game for the player
    #since the player plays first in blackjack, this function handles
    #both the opening card draw and playing the game for the player
    def draw_player(self):

        self.player.append(self.deck.pop())
        self.player.append(self.deck.pop())

        print(dedent(f"""
        Ok now it's your turn to draw. The two cards you draw are:
        {self.player}\n"""))

        while len(self.player) < 5:

            sum(self.player)
            decision = input("What do you want to do: [hit] or [stand]?  ")

            if "hit" in decision:
                self.player.append(self.deck.pop())
                print(f"Here's your hand now:\n{game.player}")

                if sum(self.player) > 21:
                    print(dedent("""
                    You went over 21. You lose"""))
                    break
                elif len(self.player) == 5:
                    print("You drew more than 5 cards without busting. You win!!!")
                    break

            elif "stand" in decision:
                print(dedent(f"Player stands, the dealer plays now"))
                break
        Game.dealer_play(self)

    #now that the player has played, this function handles the dealer playing
    #this function is also responsible for determing the ultimate outcome
    #of the game, since in blackjack the player is playing against the dealer
    #(the house), and the player's cards are compared against the dealer's
    #cards to determine who wins
    def dealer_play(self):
        print(f"Here is the player's hand:\n{self.player}")
        print('here\'s game.dealer', game.dealer)
        while len(game.dealer) < 5:
            if sum(game.dealer) > 21:
                print("Dealer busts, the player wins!")
                break
            if sum(game.dealer) == sum(self.player):
                print("The dealer wins! F the house!!")
                break
            if sum(game.dealer) > sum(self.player):
                print('The dealer wins!!', game.dealer)
                break
            game.dealer.append(self.deck.pop())





#these functions are cards to initialize the class objects, such as creating
#the deck, the game, and then starting the game, which cascades from function
#to function until completed.
deck = Cards()
game = Game(deck)
game.play()
