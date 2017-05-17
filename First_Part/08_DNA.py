def main():
      
      #open the file
      infile = open("dna.txt", "r")
      
      #read the number of pairs
      num_pairs = infile.readline()
      #strip any extra space from the read-in string
      num_pairs = num_pairs.strip()
      #convert the string to a number
      num_pairs = int(num_pairs)
      
      #print the header for the output
      print ("Longest Common Sequences")
      print ()
      
      #read each pair of dna strands, and loop through each pair
      for i in range(num_pairs):
            
            #get strand 1 in the pair
            st1 = infile.readline()
            st1 = st1.strip()
            st1 = st1.upper()
            
            #get strand 2 in the pair 
            st2 = infile.readline()
            st2 = st2.strip()
            st2 = st2.upper()
            
            #oder the strands by size
            if (len(st1) > len(st2)):
                  dna1 = st1
                  dna2 = st2
            else:
                  dna1 = st2
                  dna2 = st1
            
            #initialize a variable -- common strand for final output for each pair     
            common_strand = ""
            
            #loop through each size of the window
            wnd = len(dna2)
            while (wnd > 1):
                  
                  #use the size of the window to loop through the string starting from index 0
                  start_idx = 0    
                  while( (start_idx + wnd) <= len(dna2) ):
                        
                        #get the sub strand
                        sub_strand = dna2[start_idx : start_idx + wnd]
                        
                        #check if the sub srand in the longer DNA strand
                        if sub_strand in dna1:
                              
                              #check if the sub strand longer than the common_strand we already have 
                              if len(sub_strand) > len(common_strand) : 
                                    common_strand += sub_strand     
                              # if the sub_strand have the same length as the longest common strand
                              # and the sub_strand have not been recored, add it for final output
                              elif ( len(sub_strand) == len(common_strand) ) and ( sub_strand not in common_strand ):
                                    common_strand += "\n        "+ sub_strand
                                    
                        #increase the starting index by 1                                    
                        start_idx += 1      
                             
                  #decrease the window size by 1      
                  wnd = wnd - 1
            
            # if the two DNA share no common strand, add a "No Common Sequence Found" statement for the final output
            if (common_strand == ""):
                  common_strand  = "No Common Sequence Found"
            
            #printing the common strand for each pair      
            print ("Pair %d: "%(i+1) + common_strand) 
            print ()
      
      
main()