from collections import deque
from random import shuffle
import time

NUMBER_OF_RUNS = 1000000
stats = {}

def init():
    stats['starttime'] = time.clock()
    stats['wins'] = 0
    stats['losses'] = 0
    stats['plays'] = 0    
    
def run():
    for i in range(NUMBER_OF_RUNS):
        deck = deal()
        play(deck)
    print_results()
    
def deal():
    deck = []
    cards = [i for i in range(13) for j in range(4)]
    shuffle(cards)
    for pos in range(13):
        deck.append(deque())
        for round in range(4):
            deck[-1].append(cards.pop())
    return deck
        
def play(deck):
    card = deck[12].pop()
    kings_found = 1 if card == 12 else 0
    for i in range(51):
        deck[card].appendleft(card)
        card = deck[card].pop()
        if card == 12:
            kings_found += 1
            if kings_found == 4:
                if i == 50:
                    record_result(win=True)
                else:
                    record_result(win=False)
                break

def record_result(win=False):
    if win:
        stats['wins'] += 1
    else:
        stats['losses'] += 1
    stats['plays'] += 1

def print_results():
    with open('results.txt', 'w') as results:
        runtime = time.clock() - stats['starttime']
        results.write('Number of plays : {}\n'.format(stats['plays']))
        results.write('Number of wins  : {}\n'.format(stats['wins']))
        results.write('Number of losses: {}\n'.format(stats['losses']))
        percentage = float(stats['wins'])/stats['plays']
        results.write('Win percentage  : {:.2%}\n'.format(percentage))
        results.write('Simulation time : {:.2f}s\n'.format(runtime))

if __name__ == '__main__':
    init()
    run()
    