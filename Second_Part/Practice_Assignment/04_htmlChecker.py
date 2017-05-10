
class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return (self.items == [])

    def size(self):
        return(len(self.items))
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        return(self.items.pop())

    def peek(self):
        return(self.items[-1])

    def __str__ (self):
        return str(self.items)




#method to get the tagList
def getTag(infile):
    
    tList = []
    for line in infile:
        line = line.strip()
        
        for i in range(len(line)):
            if line[i] == "<":
                tag = ''
                for char in line[i+1:]:
                    if char == ">" or char == ' ':
                        break 
                    else:
                        tag += char
                tList.append(tag)
    return tList

#method to match the tag

def iterate(tagList):
    
    KeepStack = Stack()
    
    EXCEPTIONS = ["br", "meta","hr"]
    
    VALIDTAGS = []
    
    balanced = True
    for i in range(len(tagList)):
        
        tag = tagList[i]
        if tag not in VALIDTAGS:
            print ("New tag %s found and added to list of valid tags"%(tag))
            VALIDTAGS.append(tag)
        
        if tag in EXCEPTIONS:
            print ("Tag %s does not need to match:  stack is still %s"%(tag, str(KeepStack)))
            
        elif tag[0] != "/":
            KeepStack.push(tag)
            print ("Tag %s pushed:  stack is now %s"%(tag, str(KeepStack)))
        elif tag[0] == "/":
                tag_update = tag[1:]
                if tag_update == KeepStack.peek():
                    KeepStack.pop()
                    print ("Tag %s matches top of stack:  stack is now %s"%(tag, str(KeepStack)))    
                else:
                    print("Error:  tag is %s but top of stack is %s"%(tag, KeepStack.peek()))
                    
                    balanced = False
                    break           
        elif KeepStack.isEmpty():
                print ("Processing complete.  No mismatches found")
                
                balanced = False
                break
    
    if ( not KeepStack.isEmpty() ) and (balanced==True):
        print ("Processing complete.  Unmatched tags remain on stack:  %s"%(KeepStack))      
        
    print() 
    VALIDTAGS.sort()  
    EXCEPTIONS.sort()
     
    print ("List of VALIDTAGS :")
    print (VALIDTAGS)
    print ()
    
    print ("List of EXCEPTIONS :")
    print (EXCEPTIONS)
    print ()
       
def main():
    
    #open the file
    infile = open("04_htmlfile.txt", "r")
    #get the tag list
    tagList = getTag(infile)
    #close the file
    infile.close()
    
    #print the first 
    print ('The list of tags after reading through the file - "htmlfile.txt": ')
    print (tagList)
    print ()
    
    iterate(tagList)
    
main()


















