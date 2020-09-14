#in automate_4_2.py

import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.

    result = []
    
    for toss in range(100):
        result.append(random.randint(0, 1))
        if result[toss] == 0:
           result[toss] = 'heads'
        else:
            result[toss] = 'tails'
    
    # Code that checks if there is a streak of 6 heads or tails in a row.

    for check in range(94):
        if result[check] == result[check+1] == result[check+2] == result[check+3] == result[check+4] == result[check+5] != result[check+6]:
            numberOfStreaks += 1
        
            
print('Chance of streak: %s%%' % ((numberOfStreaks / 100) / 10000))
