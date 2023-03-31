



def multiplesOf3and5(number):

    three_div = int((number - (number % 3)) / 3) + 1
    five_div = int((number - (number % 5)) / 5) + 1
    
    threes_fives = []
    
    for i in range(three_div):
        if 3 * i < number:
            threes_fives.append(3 * i)
    
    for i in range(five_div):
        if 5 * i < number:
            threes_fives.append(5 * i)
            
    threes_fives = list(dict.fromkeys(threes_fives))
    return sum((threes_fives))


multiplesOf3and5(49)
