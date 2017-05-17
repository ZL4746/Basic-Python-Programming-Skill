def main():
      
      dimen = eval(input("Enter dimension: "))
      target = eval(input("Enter number in spiral: "))

      if dimen % 2 == 0:
            dimen = dimen+1
      if target < 1 or target > dimen**2:
            print("Number not in Range")
      
      
      outL = []
      for i in range(dimen):
            inL = []
            for i in range(dimen):
                  inL.append(0)
            outL.append(inL)
      
      #print(outL)
      
      #flag = 0 ; left 
      #flag = 1 ; right
      #flag = 2 ; up
      #flag = 3 ; down
      
      num = dimen**2
      
      #print (num)
      
      maxIndex = dimen - 1
      
      i = 0
      j = maxIndex
      flag = 0
      
      while num >= 1:
              
            if flag == 0 and j == 0:
                  flag = 3           
            elif flag == 1 and j == maxIndex:
                  flag = 2
            elif flag == 2 and i == 0:
                  flag = 0
            elif flag == 3 and i == maxIndex:
                  flag = 1
                  
            elif flag == 0 and j > 0:
                  if outL[i][j-1] != 0:
                        flag = 3          
            elif flag == 1 and j < maxIndex:
                  if outL[i][j+1] != 0:
                        flag = 2
            elif flag == 2 and i > 0:
                  if outL[i-1][j] != 0:
                        flag = 0
            elif flag == 3 and i < maxIndex:
                  if outL[i+1][j] != 0:
                        flag = 1
            
            outL[i][j] = num
            
            if flag == 0:
                  j = j - 1      
            elif flag == 1:
                  j = j + 1
            elif flag ==2:
                  i = i - 1 
            elif flag ==3:
                  i = i + 1
                  
            num -= 1
      
      #print (outL)
      
      
      for i in range(len(outL)):
            for j in range(len(outL[i])):
                  
                  if outL[i][j] == target:
                        
                        if (i>0) and (i<maxIndex) and (j>0) and (j<maxIndex):
                              
                              print (outL[i-1][j-1], outL[i-1][j], outL[i-1][j+1])
                              print (outL[i][j-1], outL[i][j], outL[i][j+1])
                              print (outL[i+1][j-1], outL[i+1][j], outL[i+1][j+1])
                        else:
                              print("Number on Outer Edge")
                              
                            
      #outer edge index 
      
      
main()

#def spiral(x):
      
      
      
      
      
      
      
      
      
      
      
      
            
      
      
      