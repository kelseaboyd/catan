import random
import time
import math

class settler:
  def __init__(self, name, longest_turn):
    self.name = name
    self.longest_turn = longest_turn

def new_deck():
    return [2,3,3,4,4,4,5,5,5,5,6,6,6,6,6,7,7,7,7,7,7,8,8,8,8,8,9,9,9,9,10,10,10,11,11,12]

game_active = True
longest_turn = 0
longest_turn_settler = "no one"
settlers = []
deck = []

num_settlers = input("How many settlers are playing? ")
print("\nEnter settlers in order of playing.")
for x in range(int(num_settlers)):
    name = input("Name? ")

    settlers.append(settler(name, 0))

while game_active:
    for s in settlers:
        if not deck:
            deck = new_deck()
            print("\n*** new deck ***")
        turn_start = input(f"\n\n{s.name}'s turn\npress enter to start ")
        if turn_start == "q":
            for s in settlers:
                print(f"{s.name}'s longest turn was {s.longest_turn}")
            quit()
        random.shuffle(deck)
        card = deck.pop()
        start = time.time()
        print(f"\nthe card is {card}\n")
        turn_end = input(f"currently {s.name}'s turn\npress enter to end turn ")
        if turn_end == "q":
            for s in settlers:
                print(f"{s.name}'s longest turn was {s.longest_turn}")
            quit()
        end = time.time()
        elapsed = end-start
        print(f"\ntime elasped in sec: {elapsed}")
        if s.longest_turn < elapsed:
            s.longest_turn = elapsed
        if longest_turn < elapsed:
            longest_turn = elapsed
            longest_turn_settler = s.name
            s.longest_turn = longest_turn
            print(f"{s.name} now has the longest turn")
        else:
            print(f"{longest_turn_settler} still has the longest turn")

