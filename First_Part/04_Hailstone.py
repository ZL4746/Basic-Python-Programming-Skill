def main():
      
      #prompt the user to enter the starting number and the ending number
      StaNum = int(input("Enter starting number of the range: "))
      EndNum = int(input("Enter ending number of the range: "))
      
      #promt the user to re enter the value if the initial values are wrong
      while ( (StaNum <= 0) or (EndNum <= 0) ):
          print("Please enter positive numbers.")
          StaNum = int(input("Enter starting number of the range: "))
          EndNum = int(input("Enter ending number of the range: "))
          
          while (EndNum <= StaNum):
              print("Starting number has to be strictly less than ending number in the range.")
              StaNum = int(input("Enter starting number of the range: "))
              EndNum = int(input("Enter ending number of the range: "))
              
      while (EndNum <= StaNum):
          print("Starting number has to be strictly less than ending number in the range.")
          StaNum = int(input("Enter starting number of the range: "))
          EndNum = int(input("Enter ending number of the range: "))
          
          while ( (StaNum <= 0) or (EndNum <= 0) ):
              print("Please enter positive numbers.")
              StaNum = int(input("Enter starting number of the range: "))
              EndNum = int(input("Enter ending number of the range: "))

      #initialize the placeholder of the number to reach the max cycle length and placeholder of the max cycle length
      numWith_max_length = 0
      max_length = 1
      
      #use the for loop to calulate cycle length of each number from the start number to the end number 
      for i in range (StaNum, EndNum + 1):
            
            flag = i
            length = 0
            while (flag > 1):
                  if flag%2 == 0:
                        flag = flag//2
                  else:
                        flag = 3*flag + 1
                  #after getting one number in the hailstone sequence, add one to the cycle length
                  length +=1
            
            #set the max value of both intended variables using comparision   
            if length >= max_length:
                  max_length = length
                  numWith_max_length = i
      

      print ("The number", numWith_max_length ,"has the longest cycle length of", str(max_length)+".")


main()