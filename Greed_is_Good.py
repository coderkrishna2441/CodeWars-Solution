# Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, 
# is to score a throw according to these rules. You will always be given an array with five six-sided 
# dice values.

'''
Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
'''

def score(dice):
    d = {}
    sum = 0
    
    # Loop for making dictonary
    for i in dice:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    # loop for getting keys and value
    for k,v in d.items():
        if d[k] >= 3:
            if k == 1:
                sum += 1000
            elif k == 6:
                sum += 600
            elif k == 5:
                sum += 500
            elif k == 4:
                sum += 400
            elif k == 3:
                sum += 300
            elif k == 2:
                sum += 200
            
            d[k] = d[k] - 3
            
            if d[k] >= 1:
                for j in range(d[k]):
                    if k == 1:
                        sum += 100
                    elif k == 5:
                        sum += 50
        else:
            for j in range(d[k]):
                if k == 1:
                    sum += 100
                elif k == 5:
                    sum += 50
    return sum