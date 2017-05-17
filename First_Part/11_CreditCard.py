def is_valid (cc_num):
      # This function checks if a credit card number is valid
      
      #convert the int input to a string
      cc_num = str(cc_num)
      
      #return not valid for card number that is not 15 or 16 digit
      if len(cc_num) != 15 and len(cc_num) != 16:
            return ("Not a 15 or 16-digit number")
            
            #    43210-98765-43210
            #15: xxxxx-xxxxx-xxxxx
            #    54321-09876-54321-0
            #16: xxxxx-xxxxx-xxxxx-x
            
      #check wether a 15 digit cardnumber is valid, by Luhn's Test
      elif len(cc_num) == 15:
            d = []
            for i in range(15):
                  d.append(int(cc_num[-1-i]))
            
            for i in range(1,14,2):
                  TwoTimes = d[i]*2
                  if TwoTimes > 9:
                        a = TwoTimes%10
                        b = TwoTimes//10
                        singleToAdd = a+b
                  else:
                        singleToAdd = TwoTimes
                  d[i] = singleToAdd
            
            sumDigit = sum(d)
            
            if sumDigit%10 == 0:
                  return True
            else:
                  return ("Invalid credit card number")
                  
      #check wether a 16 digit card number is valid, by Luhn's Test     
      elif len(cc_num) == 16:
            d = []
            for i in range(16):
                  d.append(int(cc_num[-1-i]))
            
            for i in range(1,16,2):
                  TwoTimes = d[i]*2
                  if TwoTimes > 9:
                        a = TwoTimes%10
                        b = TwoTimes//10
                        singleToAdd = a+b
                  else:
                        singleToAdd = TwoTimes
                  d[i] = singleToAdd
            
            sumDigit = sum(d) 
            if sumDigit%10 == 0:
                  return True
            else:
                  return ("Invalid credit card number")
                  

def cc_type (cc_num): 
      # This function returns the type of credit card
      # Used only after we validate a credit card number
       
      #convert the int input to a string
      cc_num = str(cc_num)
      
      #use a list to record every digit of a valid credit card number 
      d = []
      for i in range(len(cc_num)):
            d.append(int(cc_num[i]))
      
      #check the first few element of the list, to verify the card type
      if ( d[:2] == [3, 4] ) or ( d[:2] == [3, 7] ):
            return ("American Express ")
      elif (d[:4] == [6, 0, 1, 1] ) or ( d[:3] == [6, 4, 4] ) or ( d[:2] == [6 , 5] ):
            return ("Discover ")
      elif (d[0] == 5) and ( ( d[1] >= 0 ) and ( d[1] <= 5) ):
            return ("MasterCard ")
      elif (d[0] == 4):
            return ("Visa ")
      else:
            return ("")


def main():
      
      #ask the user to enter the credit card number 
      card = int(input("Enter 15 or 16-digit credit card number: "))
      print()
      
      #check the credit card number is valid or not
      if is_valid(card) == True:
            
            #verify the card type of the credit card, after verified as valid number
            cardType = cc_type (card)
            
            #print an output statement for a valid credit card number
            print ("Valid "+cardType+"credit card number")
            
      else:
            #print an output satement for an invalid credit card number
            print (is_valid(card))
            

main()