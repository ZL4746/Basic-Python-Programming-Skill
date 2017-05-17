def is_prime(num):
      
      is_prime = True
      divisor = 2
      limit = int(num**0.5) + 1
      while (divisor < limit) and is_prime:
            if (num%divisor == 0):
                  is_prime = False
            divisor += 1
      return is_prime 
      
      
def main():
      
      #prompt the user to input lower limit and upper limit 
      lo = eval(input("Enter the lower limit: "))
      up = eval(input("Enter the upper limit: "))
      
      #prompt the user to re-enter if not satisfied the condition
      while ( (lo < 4) or (up <= lo) or (lo % 2 != 0) or (up % 2 != 0) ):
            print ("Something wrong with the input, please re-enter")
            lo = eval(input("Enter the lower limit: "))
            up = eval(input("Enter the upper limit: "))
            
            
      #to print all the even number at the beginning 
      for num in range (lo, up+1, 2):
            
            #use a string for final output after one line
            sum_string = str(num)
            
            #use a loop to test the first prime number
            for i in range (2, int(num/2 + 1) ): 
                  
                  if is_prime(i):    
                        
                        #if the first number is prime, use a loop to test the second prime number
                        for j in range (int(num/2), num):
                              
                              #initialize the sum before each successful testing      
                              summing = 0 
                              if is_prime(j):
                                    summing = i + j
                              
                              #add the sum to the sum_string to eventually get output for each line      
                              if (num == summing):
                                    sum_string += (" = "+ str(i) + " + " + str(j) ) 

            #print the final sum_string after all the loop and test                              
            print (sum_string)
main()



                              
                        
      
      
      
