

class Queue (object):
   def __init__(self):
      self.items = [ ]

   def isEmpty (self):
      return self.items == [ ]

   def enqueue (self, item):
      self.items.insert(0,item)

   def dequeue (self):
      return self.items.pop ()

   def size (self):
      return len(self.items)

   def peek (self):
      return self.items [len(self.items)-1]
      
   def __str__(self):
      if len(self.items) == 0:
          return "[ ]"
      else:
          return str(self.items)
   def returnList(self):
       return self.items
       
def printqueue(Critical, Serious, Fair):
    print ( "\t Queues are: ")
    print ( "\t Critical: %s"%( str(Critical) ) )
    print ( "\t Serious:  %s"%( str(Serious) ) )
    print ( "\t Fair:     %s"%( str(Fair) ) )
    
def treat_Critical(Critical, Serious, Fair):
    print ("\t Treating %s from Critical queue"%(Critical.peek() ))
    Critical.dequeue()
    printqueue(Critical, Serious, Fair)
    print ()
    
def treat_Serious(Critical, Serious, Fair):
    print ("\t Treating %s from Serious queue"%(Serious.peek()))
    Serious.dequeue()
    printqueue(Critical, Serious, Fair)
    print ()
    
def treat_Fair(Critical, Serious, Fair):
    print ("\t Treating %s from Fair queue"%(Fair.peek()))
    Fair.dequeue()
    printqueue(Critical, Serious, Fair)
    print ()
    
   
def main():
    
    Critical = Queue()
    Serious = Queue()
    Fair = Queue()
    
    infile = open("05_ERsim.txt","r")
    
    #loop through the file line by line
    for line in infile:
        
        #strip the line for any spaces on side
        line = line.strip()
        #split the line to detect each component in the line
        temp_List = line.split(" ")
        
        #procee of adding patient to queue
        if temp_List[0] == "add":
            name = temp_List[1]
            status = temp_List[-1]
            if temp_List[-1] == "Critical":
                Critical.enqueue (name)    
            elif temp_List[-1] == "Serious":
                Serious.enqueue (name)    
            elif temp_List[-1] == "Fair": 
                Fair.enqueue (name)

            print (">>> Add patient %s to %s queue"%(name,status))
            print ()
            printqueue(Critical, Serious, Fair)
            print()
   
        
        #process of treating patient on queue
        elif temp_List[0] == "treat":
            
            #process for treat next
            if temp_List[1] == "next": 
                print (">>> Treat next patient")
                print ()
                
                if str(Critical) == "[ ]" and str(Serious) == "[ ]"  and str(Fair) == "[ ]" :
                    print ("\t No patients in queue")
                    print ()
                    
                else:
                    if str(Critical) != "[ ]" :
                        treat_Critical(Critical, Serious, Fair)

                    elif str(Critical) == "[ ]"  and str(Serious) != "[ ]" :
                        treat_Serious(Critical, Serious, Fair)
                            
                    elif str(Critical) == "[ ]"  and str(Serious) == "[ ]"  and str(Fair) != "[ ]" :
                        treat_Fair(Critical, Serious, Fair)

            #process for treat a specific queue not in regular order
            elif temp_List[1] == "Critical":
                print (">>> Treat next patient on Critical queue")
                print ()
                if str(Critical) == "[ ]" and str(Serious) == "[ ]"  and str(Fair) == "[ ]" :
                    print ("\t No patients in queues")
                    print ()
                elif str(Critical) == "[ ]" :
                    print ("\t No patients on Critical queue") #but there are patients on other queues 
                    print ()
                else:
                    treat_Critical(Critical, Serious, Fair)
            elif temp_List[1] == "Serious": 
                print (">>> Treat next patient on Serious queue")
                print ()
                if str(Critical) == "[ ]" and str(Serious) == "[ ]"  and str(Fair) == "[ ]" :
                    print ("\t No patients in queues")
                    print ()
                elif str(Serious) == "[ ]" :
                    print ("\t No patients on Serious queue") #but there are patients on other queues
                    print ()
                else:
                    treat_Serious(Critical, Serious, Fair)
            elif temp_List[1] == "Fair":
                print (">>> Treat next patient on Fair queue")
                print ()
                if str(Critical) == "[ ]" and str(Serious) == "[ ]"  and str(Fair) == "[ ]" :
                    print ("\t No patients in queues")
                    print ()
                elif str(Fair) == "[ ]":
                    print ("\t No patients on Fair queue") #but there are patients on other queues
                    print ()
                else:
                    treat_Fair(Critical, Serious, Fair)
            
            
            #process for treating all patient in regular order all at once    
            elif temp_List[1] == "all":
                print (">>> Treat all patients")
                print ()
                if str(Critical) != "[ ]" :
                    for i in range( len(Critical.returnList()) ):
                        if str(Critical) == "[ ]" :
                            break
                        else:
                            treat_Critical(Critical, Serious, Fair)
                        
                if str(Serious) != "[ ]" :
                    for i in range( len(Serious.returnList()) ):
                        if str(Serious) == "[ ]" :
                            break
                        else:
                            treat_Serious(Critical, Serious, Fair)
                        
                if str(Fair) != "[ ]" :
                    for i in range( len(Fair.returnList()) ):
                        if str(Fair) == "[ ]" :
                            break
                        else:
                            treat_Fair(Critical, Serious, Fair)
                                                
                print ("\t No patients in queues")
                print ()
                
            elif temp_List[0] == "Exit":
                print (">>> Exit")
                break     
                
    infile.close()   
    
main()  
      
      
      