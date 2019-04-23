import itertools
import random

match_conditions = {1: "Suite",
                    2: "Face value",
                    3: "Both"}

suites = ('Hearts', 'Spades', 'Diamonds', 'Clubs')
values = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

print "\nWelcome to Snapster!!"
print "====================="
for key, value in match_conditions.items():
    print "{}: {}".format(key, value)

condition = int(input("\nChoose a condition (1-3): "))
print "\nYou have chosen '{}' as your match condition\n".format(match_conditions[condition])

num_packs = int(input("Choose number of packs: "))
print "\nYou have chosen to use {} packs\n".format(num_packs)

cards = [card for card in list(itertools.product(suites, values)) for _ in range(num_packs)]

scores = {"player1": 0,
          "player2": 0}

def check_card(cards_in_play, condition):
    if len(cards_in_play) < 2: return
    if condition < 3:
        if cards_in_play[-1][condition - 1] == cards_in_play[-2][condition - 1]:
            print "Snap!!"
            return True
    else:
        if ":".join(cards_in_play[-1]) == ":".join(cards_in_play[-2]):
            print "Snap!!"
            return True

    return False

cards_in_play = []

while len(cards) > 0:
    current_player = "player1"
    p1card = random.choice(cards)
    print "Player 1 draws {}".format(p1card)
    cards_in_play.append(p1card)
    cards.remove(p1card)

    if check_card(cards_in_play, condition):
        scores[current_player] += len(cards_in_play)
        cards_in_play = []

    current_player = "player2"
    p2card = random.choice(cards)
    print "Player 2 draws {}".format(p2card)
    cards_in_play.append(p2card)
    cards.remove(p2card)

    if check_card(cards_in_play, condition):
        scores[current_player] += len(cards_in_play)
        cards_in_play = []

print "\nScores: ", scores

if scores['player1'] > scores['player2']:
    print "\nPlayer 1 WINS!!"
else:
    print "\nPlayer 2 WINS!!"

