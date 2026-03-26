# AIML-PROJECT

# 🃏 Blackjack — Terminal Card Game

A fully playable **Blackjack game in the terminal**, written in Python using only the built-in `random` library. Play against an AI dealer with real chip betting, ace adjustment logic, and classic casino rules.


## 📸 Preview

```
=== Chips: 85 ===
Place your bet: 20

Dealer shows: King of Spades
Your hand: ['Seven of Hearts', 'Nine of Clubs'] = 16

Hit or Stand? (h/s): h
Your hand: 19

Dealer: 18  |  You: 19
You win! 🎉
```


## ✨ Features

- **Deck shuffling** — 52-card deck built and shuffled with `random.shuffle`
- **Hit / Stand logic** — Full player turn control
- **Dealer AI** — Dealer hits on ≤16, stands on 17+ (Vegas rules)
- **Ace adjustment** — Aces auto-switch from 11 → 1 to prevent bust
- **Chip & betting system** — Start with 100 chips, bet each round
- **Bust & win detection** — Handles player bust, dealer bust, push (tie)
- **Auto-reshuffle** — Deck reshuffles when fewer than 15 cards remain


## 🗂️ Project Structure

```
blackjack/
├── blackjack.py     # Main game file (all classes + game loop)
└── README.md        # You're here
```


## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- No external libraries needed — only `random` (built-in)

### Run the game

```bash
git clone https://github.com/your-username/blackjack.git
cd blackjack
python blackjack.py
```

## 🧱 How It's Built

The game is structured around 5 classes:

| Class | Responsibility |
|-------|---------------|
| `Card` | Stores suit, rank, and value |
| `Deck` | Builds 52-card deck, shuffles, deals |
| `Hand` | Holds cards, tracks total, handles ace logic |
| `Player` | Manages chips, bet placement, win/loss payouts |
| `Dealer` | Holds hand, applies AI hit/stand rule |

### Ace Logic

Aces start at 11. If the hand total exceeds 21 and an ace is present, it drops to 1 automatically:

```python
def adjust_for_ace(self):
    while self.value > 21 and self.aces:
        self.value -= 10
        self.aces -= 1
```


## 🎮 Game Rules

- You and the dealer each start with 2 cards
- Dealer's second card is hidden until your turn ends
- **Hit** to draw another card, **Stand** to hold
- Closest to 21 without going over wins
- Dealer must hit on 16 or less, stand on 17 or more
- Going over 21 = **bust** = instant loss


## 🔧 Stretch Goals (Coming Soon)

- [ ] Blackjack natural — 3:2 payout on Ace + 10-value card
- [ ] Double Down — double the bet, receive exactly one more card
- [ ] Split — split a pair into two separate hands
- [ ] Session history — save win/loss record to a JSON file
- [ ] Color output — use `colorama` for colored terminal display


## 📚 Concepts Covered

This project is a practical exercise in:

- **Object-Oriented Programming** — classes, `__init__`, `__str__`
- **Randomness** — `random.shuffle`, `random.seed`
- **Control flow** — while loops, early returns, conditionals
- **Input validation** — `try/except` for non-numeric input
- **State management** — tracking hand totals and chip balances


## 📄 License

This project is open source under the [MIT License](LICENSE).


## 🙌 Acknowledgements

Built as part of a self-guided Python learning project. Inspired by classic casino Blackjack rules.
