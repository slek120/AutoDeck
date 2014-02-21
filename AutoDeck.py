from random import randint
from time import clock

# Algorithm timer
start = clock()

# Cost limit
maxCost = 72
# Deck size
maxCards = 9

# List of cards with [Hp, Atk, Cost]
##collection = [
##    [780,390,13],
##    [941,294,7],
##    [787,393,7],
##    [728,448,7],
##    [750,235,9],
##    [598,389,9],
##    [485,306,7],
##    [620,263,8],
##    [769,231,9],
##    [500,256,7],
##    [609,396,9],
##    [627,379,9],
##    [793,306,10],
##    [744,240,9],
##    [421,259,4],
##    [517,160,4],
##    [450,225,4],
##    [299,190,3],
##    [360,141,3],
##    [318,188,3],
##    [480,190,4],
##    [475,192,4],
##    [305,192,3],
##    [565,282,5],
##    [480,192,4],
##    [330,169,3],
##    [420,253,4],
##    [448,219,4],
##    [612,240,5],
##    [512,160,4]
##    ]

# Test with 10,000 cards
collection = [ [randint(300,800), randint(150,400), randint(3,13)] for i in range(10000)]

# The result
deck = []

# What to use to calculate value
def getValue(card):
    #return card[0] # Focus on Hp
    #return card[1] # Focus on Atk
    #return 5*card[0] + 11*card[1] # Custom balance
    return card[0]+card[1] # Equal balance

# Sort from least cost efficient to most cost efficient
def ValuePerCost(card):
    # Value / Cost
    return getValue(card)/card[2]

# Sort collection by efficiency
collection.sort(key=ValuePerCost)

# Take the first 9 most cost efficient cards
for i in range(maxCards):
    # Check if adding the next card doesn't exceed cost limit
    if( sum([x[2] for x in deck]) + collection[-1][2] <= maxCost ): # -1 = last in list
        deck.append(collection.pop())

# Go through collection to see if value can be added
while( len(collection) > 0 ):
    index = -1
    value = sum([getValue(card) for card in deck])
    # Go through deck to see what adds most value
    for i in range(len(deck)):
        # Check if replacement doesn't exceed cost limit
        if( sum([card[2] for card in deck]) - deck[i][2] + collection[-1][2] <= maxCost ):
            # Check if replacement adds value
            if( sum([getValue(card) for card in deck]) - getValue(deck[i]) + getValue(collection[-1]) > value ):
                # Replace card that adds most value
                value = sum([getValue(card) for card in deck]) - getValue(deck[i]) + getValue(collection[-1])
                index = i
    # Replace if value is added
    if( index != -1 ):
        deck.pop(index)
        deck.append(collection.pop())
    else:
        collection.pop()

print(deck)
print("Total Value: " + str(sum([getValue(x) for x in deck])))
print("HP:  " + str(sum([x[0] for x in deck])) + "\t#:  " + str(len(deck)))
print("ATK: " + str(sum([x[1] for x in deck])) + "\tCP: " + str(sum([x[2] for x in deck])))
print("Calc Time: " + str(clock() - start))
