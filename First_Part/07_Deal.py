def ReturnView(Prize,Guess):
      # a function to return the View
      
      if (Prize == Guess):
            
            if (Guess == 3):
                  View = 1
            else:
                  View = Guess + 1
      else:
            if (Guess == 3 and Prize == 2) or (Guess == 2 and Prize ==3):
                  View = 1
            elif (Guess == 2 and Prize ==1) or (Guess ==1 and Prize ==2):
                  View = 3
            else:
                  View = 2
      
      return View

def NewGuess(Guess,View):
      
      #the function to return the new guess 
      
      if (Guess == 3 and View == 2) or (Guess == 2 and View ==3):
            NewGuess = 1
      elif (Guess == 2 and View ==1) or (Guess ==1 and View ==2):
            NewGuess = 3
      else:
            NewGuess = 2
      
      return NewGuess


import random

def main():
      
      n = eval(input( "Enter number of times you want to play: " ))
      print ()
      
      n_winning = 0
                  
      #print the header
      print ("  Prize      Guess       View    New Guess")
      
      #repeat the game based on the number entered 
      for i in range(1,n+1):
            
            #get the prize
            Prize = random.randint(1,3)
            
            #get the Guess
            Guess = random.randint(1,3)
            
            #get the View 
            View2 = ReturnView(Prize, Guess)
            
            #get the new Guest
            Next_Guest = NewGuess(Guess,View2)
            
            #increase the winning times if new Guest is the prize 
            if Next_Guest == Prize:
                  n_winning += 1
            
            #print the result
            print("%5d%11d%11d%11d"%(Prize,Guess,View2,Next_Guest))
      
      #get the probability required
      p_switch = n_winning/n
      p_keep = 1- p_switch
      
      print()
      print("Probability of winning if you switch = %.2f"%(p_switch) )
      print("Probability of winning if you do not switch = %.2f"%(p_keep) )
                  
                  
main()
            

            