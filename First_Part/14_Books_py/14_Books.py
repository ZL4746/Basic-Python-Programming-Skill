word_dict = {}
def create_word_dict ():
      # Create word dictionary from the comprehensive word list      
      infile = open("words.txt","r")
      for word in infile:
            word = word.strip()
            word_dict[word] = 1
      infile.close()
       

# Removes punctuation marks from a string
def parseString (st):
      
      st2 = st
      st2 += "   "
      
      new_str = ''
      
      i = 0 # a string index
      while i < len(st2)-3:
            
            char = st2[i]
            char2 = st2[i+1]
            char3 = st2[i+2]
            
            if char.isalpha() or char.isspace():
                  new_str += char
                  i += 1
            elif char == "-":
                  new_str += " "
                  i += 1
            elif (char == "’" or char == "'") and char2 == "s" and char3== " ":
                  new_str += " "
                  i += 3
            elif (char == "’" or char == "'") and char2 ==" ":
                  new_str += " "
                  i += 2
            elif (char == "’" or char == "'") and char2.isalpha():
                  new_str += char
                  i += 1
            else:
                  new_str += " "
                  i += 1
                  
      return (new_str)
      

# Returns a dictionary of words and their frequencies
def getWordFreq (file):
      
      freq_dict = {}
      infile = open(file,"r")
      
      for line in infile:
            line = line.strip()
            if line == '':
                  continue
                  
            line = parseString(line)
            line = line.strip()
            word_list = line.split()
            for word in word_list:
                  freq_dict[word] = freq_dict.get(word, 0) + 1
                  
      cap = []
      temp = []
      for word in freq_dict:
            if word[0].isupper():
                  cap.append(word)
                  temp.append(word)
      for word in cap:
            if word.lower() in freq_dict:
                  freq_dict[word.lower()] += 1
            elif word.lower() in word_dict:
                  freq_dict[word.lower()] = 1   # +freq_dic.get(word.lower(),0)
      for word in temp:
            del freq_dict[word]
            
      infile.close()
      del cap
      del temp
      return freq_dict
      
  
# Compares the distinct words in two dictionaries
def wordComparison (author1, freq1, author2, freq2):
      
      D_key_len = len(freq1.keys())
      D_total = int(sum(freq1.values()))
      D_ratio = round(D_key_len / D_total * 100, 10)
      
      print (author1)
      print ("Total distinct words = ", D_key_len )
      print ("Total words (including duplicates) = ", D_total)
      print ("Ratio (% of total distinct words to total words) = ", D_ratio) 
      print ()
      
      H_key_len = len(freq2.keys())
      H_total = int(sum(freq2.values()))
      H_ratio = round(H_key_len / H_total * 100, 10)
      
      print (author2)
      print ("Total distinct words = ", H_key_len )
      print ("Total words (including duplicates) = ", H_total)
      print ("Ratio (% of total distinct words to total words) = ", H_ratio)
      print ()
      
      D = set (freq1.keys())
      H = set (freq2.keys())
      DminH = D - H
      HminD = H - D
      
      D_diff = 0
      for word in DminH:
            D_diff += freq1[word]
            
      H_diff = 0
      for word in HminD:
            H_diff += freq2[word]
            
      rate1 = round(D_diff / D_total * 100, 10)
      rate2 = round(H_diff / H_total * 100, 10)
      
      print (author1, 'used', len(DminH), 'words that', author2, 'did not use.')
      print ('Relative frequency of words used by '+ author1 + ' not in common with '+author2 + ' = ', rate1)
      print()
      print (author2, 'used', len(HminD), 'words that', author1, 'did not use.')
      print ('Relative frequency of words used by '+ author2 + ' not in common with '+author1 + ' = ', rate2)
      print ()

def main():
      # Create word dictionary from comprehensive word list
      create_word_dict()

      # Enter names of the two books in electronic form
      book1 = input ("Enter name of first book: ")
      book2 = input ("Enter name of second book: ")
      print()

      # Enter names of the two authors
      author1 = input ("Enter last name of first author: ")
      author2 = input ("Enter last name of second author: ")
      print() 
  
      # Get the frequency of words used by the two authors
      wordFreq1 = getWordFreq (book1)
      wordFreq2 = getWordFreq (book2)
      
      # Compare the relative frequency of uncommon words used
      # by the two authors
      wordComparison (author1, wordFreq1, author2, wordFreq2)
      
  
main()