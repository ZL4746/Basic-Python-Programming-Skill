
def graphy(list1):
    
    list2 = []
    larggest = max(list1)
    for h in range(larggest):
        inlist = "|"
        for i in range (len(list1)):
            if list1[i] > 0:
                inlist += "  *"
                list1[i] -= 1
            else:
                inlist += "   "
        list2.append(inlist)
    list2.reverse()
    list2.append("+--+--+--+--+--+--+--+--+--+--+--+-\n"+"   2  3  4  5  6  7  8  9 10 11 12")
    
    return list2


import random
def main():
    
    random.seed(1314)
    
    times = eval(input("How many times do you want to roll the dice? "))
              #0,1,2,3,4,5,6,7,8,9,0
              #2,3,4,5,6,7,8,9,0,1,2
    results = [0,0,0,0,0,0,0,0,0,0,0] 
              
    for i in range(times):
        
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        diceSum = dice1 + dice2
        #print (dice1,dice2,diceSum)
        
        results[diceSum-2] += 1
        
    print("Results: ", results)
    
    if times <= 100:
        list_in = results
    else:
        list_in = []
        for item in results:
            x = int( round( item/(times/100) ) )
            list_in.append(x)
            
    graph = graphy(list_in)
    
    for line in graph:
        print (line)
    
main() 
    

    