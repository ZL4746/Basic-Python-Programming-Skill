def main():
      # create an empty dictionary
      pop_freq = {}
      
      # initialize the dictionary
      pop_freq ['1'] = 0
      # fill the rest
      pop_freq ['9'] = 0

      # open file for reading
      in_file = open ("13_Census_2009.txt", "r")

      # read the header and ignore
      header = in_file.readline()
      
      #initilized a counter of total
      Total = 0

      # read subsequent lines
      for line in in_file:
        line = line.strip()
        pop_data = line.split()
        # get the last element that is the population number
        pop_num = pop_data[-1]
        Total += 1
        
        fDigit = pop_num[0]

        # make entries in the dictionary
        if fDigit in pop_freq:
              pop_freq[fDigit] = pop_freq[fDigit] + 1
        else:
              pop_freq[fDigit] = 1

      # write out the result
      print("Digit	Count	%")
      all_digits = list(pop_freq.keys())
      all_digits.sort()
      for digit in all_digits:
            percentage = pop_freq[digit]*100/Total
            print(digit+"	"+str(pop_freq[digit])+"	"+"%.1f"%(percentage))
            
      # close the file
      in_file.close()

  
main()