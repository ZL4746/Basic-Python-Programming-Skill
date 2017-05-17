def Validate_ISBN_Char(AList):
      #A fucntion just for validating character in the ISBN, excluding "-"
      
      #get the first 9 characters
      string9 = ""
      for char in (AList[:8]):
            string9 += char
      
      #return true for the exactly right format
      if (len(AList) == 10) and (string9.isdigit()) and ( AList[9] == "X" or AList[9] == "x" or AList[9].isdigit() ):
            return True
      else:
            return False

def PartialSum(AList):
      
      #initialized a list for getting each partial sum
      PartialSum = []
      
      #initial a number for calculating partial sum
      #and loop through the list to the partial sum
      Psum = 0
      for char in AList:
            if char == 'X' or char == 'x':
                  Psum += 10
                  PartialSum.append(Psum)      
            else:
                  Psum += int(char)
                  PartialSum.append(Psum)
                  
      return PartialSum
                        
def main():
      
      infile = open("isbn.txt","r")
      outfile = open("isbnOut.txt","w")
      
      
      #loop through each line in the infile
      for ISBN in infile:
            
            ISBN = ISBN.strip()
            string_list = []
            
            #loop through the character of one ISBN
            for char in ISBN:
                  if char != "-":
                       string_list.append(char)
            
            #use the function to validate the format of the ISBN           
            if Validate_ISBN_Char(string_list) == True:
                  #print (string_list)
                  
                  s1 = PartialSum(string_list)
                  #print(s1)
                  s2 = PartialSum(s1)
                  #print(s2)
                  
                  #test the last number of the partial sum S2
                  if (s2[-1]%11) == 0:
                        outfile.write(ISBN+"  "+"valid"+"\n")
                  else:
                        outfile.write(ISBN+"  "+"invalid"+"\n")
                        
            elif Validate_ISBN_Char(string_list) == False:
                  outfile.write(ISBN+"  "+"invalid"+"\n")
                  
      infile.close()    
      outfile.close()      

main()


            
                        
                  
      
      