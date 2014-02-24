from random import randint
from time import clock

# Algorithm timer
start = clock()

# Cost limit
maxCost = 72
# Deck size
maxCards = 9

# List of cards with [Hp, Atk, Cost]
collection = [
    [780,390,13],
    [941,294,7],
    [787,393,7],
    [728,448,7],
    [750,235,9],
    [598,389,9],
    [485,306,7],
    [620,263,8],
    [769,231,9],
    [500,256,7],
    [609,396,9],
    [627,379,9],
    [793,306,10],
    [744,240,9],
    [421,259,4],
    [517,160,4],
    [450,225,4],
    [299,190,3],
    [360,141,3],
    [318,188,3],
    [480,190,4],
    [475,192,4],
    [305,192,3],
    [565,282,5],
    [480,192,4],
    [330,169,3],
    [420,253,4],
    [448,219,4],
    [612,240,5],
    [512,160,4]
    ]

# Test with 1,000 cards
#collection = [ [randint(300,800), randint(150,400), randint(3,13)] for i in range(1000)]

# Create a list of decks where decks[i][j] is the highest value deck for total cards up to 'i' and total cost up to 'j'
# Decks[0][0] has total cards 0 and total cost 0 so highest possible value is 0
# Decks are built from previous lower card and lower cost decks
# Decks are in the form [k_1, k_2,..., k_n] where k_i is True or False
# If k_i is True, collection[i] is used in the deck
decks = [[[False for k in range(len(collection))] for j in range(maxCost+1)] for i in range(maxCards+1)]

# What to use to calculate value
def getValue(card):
    #return card[0] # Focus on Hp
    #return card[1] # Focus on Atk
    #return 5*card[0] + 11*card[1] # Custom balance
    return card[0]+card[1] # Equal balance

# What to use to calculate cost
def getCost(card):
    return card[2]

# Get the total value for a given deck
def getDeckValue(deck):
    total = 0
    for i, card in enumerate(deck):
        if(card):
            total += getValue(collection[i])
    return total

# Get the total cost for a given deck
def getDeckCost(deck):
    total = 0
    for i, card in enumerate(deck):
        if(card):
            total += getCost(collection[i])
    return total

# Count the number of cards used in a given deck
def getDeckCount(deck):
    total = 0
    for card in deck:
        if(card):
            total += 1
    return total

# Convert a deck into a list of cards from collection
def makeDeck(deck):
    return [collection[i] for i,card in enumerate(deck) if card]

#Build decks starting from 1 to maxCards
for n in range(1,maxCards+1):
    # Use deck with 1 less card as basis
    decks[n] = list(decks[n-1])
    # Build decks starting from 1 to maxCost
    for i in range(1,maxCost+1):
        # Use the previous deck as a basis
        decks[n][i] = list(decks[n][i-1])
        # Go through collection to see if value can be added
        for j in range(len(collection)):
            # If cost of card is greater than total cost, skip
            if(getCost(collection[j]) <= i):
                # Check if previous deck can add a card without going over total cards
                if( getDeckCount(decks[n][i-getCost(collection[j])]) < n ):
                    # Use the deck where adding this card would give total cost of i
                    testDeck = list(decks[n][i-getCost(collection[j])]) # Copy deck
                    testDeck[j] = True # Add card
                    # Check if value is added
                    if( getDeckValue(testDeck) > getDeckValue(decks[n][i]) ):
                        decks[n][i] = list(testDeck) # Copy deck
                else:
                    # Use the deck where there is space for adding a card
                    testDeck = list(decks[n-1][i-getCost(collection[j])]) # Copy deck
                    testDeck[j] = True # Add card
                    # Check if value is added
                    if( getDeckValue(testDeck) > getDeckValue(decks[n][i]) ):
                        decks[n][i] = list(testDeck) # Copy deck

deck = makeDeck(decks[n][maxCost])
print(deck)
print("Total Value: " + str(sum([getValue(x) for x in deck])))
print("HP:  " + str(sum([x[0] for x in deck])) + "\t#:  " + str(len(deck)))
print("ATK: " + str(sum([x[1] for x in deck])) + "\tCP: " + str(sum([x[2] for x in deck])))
print("Calc Time: " + str(clock() - start))
