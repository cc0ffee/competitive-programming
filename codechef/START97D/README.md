## START97D

This is where I review the problems I have done.

### RIP2000

> Chef had collected N notes of Rs. 2000 to pay his total college fees. However, the government banned Rs. 2000 notes. Chef wants to pay the same amount using Rs. 500 notes only. Find the number of notes Chef needs.

This was a simple math problem. What I considered was getting the total value of notes (eg 4 notes is 8000) and dividing it by 500 to get the amount of 500 notes needed. It was correct.

### Best of Two

> Alice and Bob are playing a game. Each player rolls a regular six faced dice 3 times. The score of a player is the sum of the values of the highest 2 rolls. The player with the highest score wins, and the game ends in a Tie if both players have the same score. Find the winner of the game or determine whether it is a tie.

First I was trying to figure out how to accept multiline inputs in python, because I haven't done something like that. I put each line seperated into an array, which was convienent since each line was respresenting a different input.

After getting the number of test cases, I looped through each test case to get Alice's scores first, then to find the minimum value to then subtract that from the addition of all scores. I did the same thing for Bob, then I compared the two scores.

There was some better ways to do this problem. The most important was that I could have just mapped the input into the neccessary values rather than putting them in an array. Someone did decide to just sort the scores, and I found out that it is as efficient as using the min function which is O(n), but it was probably an easier and shorter way to just use sort.
