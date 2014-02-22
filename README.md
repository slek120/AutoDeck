#AutoDeck

Create a deck with a card limit and cost limit from a collection of cards

GreedyDeckBuilder.py uses a variation of the Greedy approximation algorithm of the [Knapsack problem](http://en.wikipedia.org/wiki/Knapsack_problem#Greedy_approximation_algorithm)


0-1KnapsackDeckBuilder.py uses a variation of the dynamic programming method of the [Knapsack problem](http://en.wikipedia.org/wiki/Knapsack_problem#0.2F1_Knapsack_Problem)

MultidimensionalKnapsackDeckBuilder.py is the same as 0-1KnapsackDeckBuilder.py but uses a simpler method that uses an additional dimension which increases the list's size and iteration time

Descriptions:
===============================
Many social games have a system where you can choose a team of up to a set number of cards.
The additional limit of cost, usually correlated with your rank or level, prevents you from just choosing the best cards.

The Greedy method give a decently optimal solution in a short amount of time.
O(n) algorithm that takes average 0.8s for 10,000 cards.

The 0/1 Knapsack problem gives a solution with the optimal value.
O(nW) algorithm that takes average 1s for 100 cards.

*Using max cost of 72 and deck size of 9

Greedy Approximation
===============================

Procedure: 
-------------------------------
1. Choose the most cost optimal team
2. If this team fills up the cost, the algorithm is done and this is the most optimal team
3. If there is cost left over, take the next cost optimal card and replace the card that adds most value
 
アルゴリズム:
-------------------------------
1. コスト効率の高いチームをまず選ぶ
2. 最大コスト超えていたらこのチームが最適
3. コスト残っていれば次に効率高いカードを選び、一番価値が上がるカードと交換

0/1 Knapsack Problem
===============================

Procedure: 
-------------------------------
1. Create a list of best value decks for total cost from 0 to max cost
2. Start with total cost 0
3. Best value for total cost 0 is 0
4. Add 1 to total cost
5. Go through each card in collection
6. See if adding card to deck with total cost - this card's cost gives best value
7. If the number of cards exceeds deck size, see if replacing a card from deck with total cost - cost difference in replacement gives best value
8. Repeat steps 4-7
9. Once total cost reaches max cost, the deck with best value is created

アルゴリズム:
-------------------------------
1. 総コスト０から最大総コストまでの最高価値のデッキのリストを作成
2. コストを０から始める
3. 総コストが０だと最大価値は０
4. 総コストを１増やす
5. コレクションのカードを反復する
6. カードを（総コスト－カードコスト）のデッキに入れて、価値が上がったら最高価値デッキにする
7. デッキが最大枚数を超えたら（総コスト－交換カードのコストの差）のデッキで交換して、価値が上がったら最高価値デッキにする
8. 4~7を繰り返す
9. 総コストが最大コストに達すると最大価値のデッキを組みました

Multi-dimensional Knapsack
===============================
The procedure is the same as the 0/1 knapsack except in step 7:

* If the number of cards exceeds deck size, see if adding card to deck with total cards - 1 gives best value.

アルゴリズムは0/1ナップサック問題と同じです。近いはステップ7だけです：

* デッキが最大枚数を超えたら（枚数－1）のデッキに入れて、価値が上がったら最高価値デッキにする
