AutoDeck
========

Create a deck with a card limit and cost limit from a collection of cards


Descriptions:
-------------------------------
Many social games have a system where you can choose a team of up to a set number of cards.
The additional limit of cost, usually correlated with your rank or level, prevents you from just choosing the best cards.
This is an example algorithm to get a decently optimal team.
O(n) algorithm that takes average 0.8s for 10,000 cards.

Procedure: 
-------------------------------
1. Choose the most cost optimal team
2. If this team fills up the cost, the algorithm is done and this is the most optimal team
3. If there is cost left over, take the next cost optimal card and replace the card that adds most value
 
アルゴリズム:
-------------------------------
1. コスト効率の高いチームをまず選ぶ
2. 最大コスト超えていたらこのチームが最適
3. コスト残っていれば次に効率高いカードを選び、一番値が増えるカードと交換
