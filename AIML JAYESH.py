import random

suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6,
          'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10,
          'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.deck = [Card(s, r) for s in suits for r in ranks]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()
    
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0  # track aces separately

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace':
            self.aces += 1
        self.adjust_for_ace()

    def adjust_for_ace(self):
        # Downgrade an Ace from 11 to 1 if we're over 21
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Player:
    def __init__(self, name, chips=100):
        self.name = name
        self.hand = Hand()
        self.chips = chips
        self.bet = 0

    def place_bet(self, amount):
        if amount > self.chips:
            print("Not enough chips!")
            return False
        self.bet = amount
        self.chips -= amount
        return True

    def win_bet(self):
        self.chips += self.bet * 2

    def push(self):              # tie — return the bet
        self.chips += self.bet

class Dealer:
    def __init__(self):
        self.hand = Hand()

    def should_hit(self):
        # Classic dealer rule: hit on soft 16 or less
        return self.hand.value < 17

def play_round(player, deck):
    dealer = Dealer()

    # Initial deal — two cards each
    for _ in range(2):
        player.hand.add_card(deck.deal())
        dealer.hand.add_card(deck.deal())

    print(f"\nDealer shows: {dealer.hand.cards[0]}")
    print(f"Your hand: {[str(c) for c in player.hand.cards]} = {player.hand.value}")

    # Player's turn
    while True:
        action = input("\nHit or Stand? (h/s): ").lower()
        if action == 'h':
            player.hand.add_card(deck.deal())
            print(f"Your hand: {player.hand.value}")
            if player.hand.value > 21:
                print("Bust! Dealer wins.")
                return
        else:
            break

    # Dealer's turn
    while dealer.should_hit():
        dealer.hand.add_card(deck.deal())

    # Resolve
    p, d = player.hand.value, dealer.hand.value
    print(f"\nDealer: {d}  |  You: {p}")
    if d > 21 or p > d:
        print("You win!")
        player.win_bet()
    elif p == d:
        print("Push!")
        player.push()
    else:
        print("Dealer wins.")

def main():
    player = Player("You", chips=100)
    deck = Deck()
    deck.shuffle()

    while player.chips > 0:
        print(f"\n=== Chips: {player.chips} ===")

        # Re-shuffle when deck gets thin
        if len(deck.deck) < 15:
            deck = Deck()
            deck.shuffle()
            print("(Deck reshuffled)")

        try:
            bet = int(input("Place your bet: "))
        except ValueError:
            continue

        if not player.place_bet(bet):
            continue

        player.hand = Hand()   # reset hand each round
        play_round(player, deck)

    print("Out of chips. Game over!")

if __name__ == "__main__":
    main()                            