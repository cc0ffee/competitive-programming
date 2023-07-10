# cook your dish here
import sys
user_input = sys.stdin.readlines()

scores = []
for values in user_input:
   scores.append([int(value) for value in values.split()])
test_cases_range = scores[0][0]
for i in range(1, test_cases_range+1):
    a, b, c = scores[i][0], scores[i][1], scores[i][2]
    lowest_number = min(a,b,c)
    alice_score = (a+b+c) - lowest_number
    
    a, b, c = scores[i][3], scores[i][4], scores[i][5]
    lowest_number = min(a,b,c)
    bob_score = (a+b+c) - lowest_number
    
    if bob_score > alice_score:
        print("Bob")
    elif alice_score > bob_score:
        print("Alice")
    else:
        print("Tie")