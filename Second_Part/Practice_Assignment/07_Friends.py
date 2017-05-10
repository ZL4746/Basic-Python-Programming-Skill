

class Node (object):
    
    def __init__(self,initdata):
        self.data = initdata
        self.next = None            # always do this – saves a lot
                                   # of headaches later!
    def getData (self):
        return self.data            # returns a POINTER

    def getNext (self):
        return self.next            # returns a POINTER

    def setData (self, newData):
        self.data = newData         # changes a POINTER

    def setNext (self,newNext):
        self.next = newNext         # changes a POINTER
   

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty (self):
        return self.head == None

    def add (self,item):
        # add a new Node to the beginning of an existing list
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def length (self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
        
    def search (self,item):
        current = self.head
        found = False
        while current != None and not found:    
            if current.getData().name == item:
                found = True              
            else:
                current = current.getNext()
        return found
       
    def remove (self,item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData().name == item:
                found = True
            else:
                previous = current
                current = current.getNext()
                
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext() )
                    
    def getObject (self,string): 
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.getData().name == string:
                found = True
                return current.getData()
            else:
                current = current.getNext()

class User:
    
    def __init__(self, namestring):
        self.name = namestring
        self.friends = UnorderedList()
        
    def __str__(self):
        outputstr = '[ '
        current = self.friends.head
        while current != None:
            outputstr += (current.getData().name + ' ')
            current = current.getNext()
        outputstr += ']'
        return outputstr

        
def main():
    
    UserRecord = UnorderedList()
    
    infile = open("07_FriendData.txt","r")
    
    num_line = 0
    for line in infile:
        num_line += 1
        line = line.strip()
        print ("--> "+line)
        
        line_list = line.split( )
        command = line_list[0]
        
        if command == "Person":
            name = line_list[1]
            if UserRecord.search(name) == True:
                #user are in record
                print ("    A person with name %s already exists."%(name))
            else:
                tempObject = User(name)
                UserRecord.add(tempObject)
                print ("    %s now has an account."%(name))
                    
        elif command == "Friend":
            name1 = line_list[1]
            name2 = line_list[2]
            if name1 == name2:
                print ("    A person cannot friend him/herself.")
                
            #check if the name is in user record 
            elif UserRecord.search(name1) == False:
                #name1 are not in record
                print ("    A person with name %s does not currently exist."%(name1))
            elif UserRecord.search(name2) == False:
                #name2 are not in record
                print ("    A person with name %s does not currently exist."%(name2))
            else:
                #both names are in record
                # check if already friend, if not, add friend
                
                #get the user object from the record
                name1_Object = UserRecord.getObject(name1)
                name2_Object = UserRecord.getObject(name2)
                if name2_Object.friends.search(name1) == True:
                    print ("    %s and %s are already friends."%(name1, name2))
                else:
                    #add the user object to each account 
                    name1_Object.friends.add(name2_Object)
                    name2_Object.friends.add(name1_Object)
                    print ("    %s and %s are now friends."%(name1, name2))
                      
        elif command == "Unfriend":
            
            name1 = line_list[1]
            name2 = line_list[2]
            if name1 == name2:
                print ("    A person cannot unfriend him/herself.")
            elif UserRecord.search(name1) == False:
                #name1 are not in record
                print ("    A person with name %s does not currently exist."%(name1))
            elif UserRecord.search(name2) == False:
                #name2 are not in record
                print ("    A person with name %s does not currently exist."%(name2))
            else:
                #both names are in record
                # check if already friend, if friend, remove friend
                
                #get the user object from the record
                name1_Object = UserRecord.getObject(name1)
                name2_Object = UserRecord.getObject(name2)
                if name2_Object.friends.search(name1) == True:
                    #remove the user object from each account 
                    name2_Object.friends.remove(name1)
                    name1_Object.friends.remove(name2)
                    print ("    %s and %s are no longer friends."%(name1, name2))    
                else:
                    print ("    %s and %s aren't friends, so you can't unfriend them."%(name1, name2))
                    
        
        elif command == "List":
            name = line_list[1]
            if UserRecord.search(name) == False:
                #name1 are not in record
                print ("    A person with name %s does not currently exist."%(name))
            else:
                name_Object = UserRecord.getObject(name)
                if str(name_Object) == "[ ]":
                    print ("    %s has no friends."%(name))
                else:
                    print ("    "+str(name_Object))
   
        elif command == "Query":
            name1 = line_list[1]
            name2 = line_list[2]
            if name1 == name2:
                print ("    A person cannot query him/herself.")
            elif UserRecord.search(name1) == False:
                #name1 are not in record
                print ("    A person with name %s does not currently exist."%(name1))
            elif UserRecord.search(name2) == False:
                #name2 are not in record
                print ("    A person with name %s does not currently exist."%(name2))
            else:
                #both names are in record
                
                #get the user object from the record
                name1_Object = UserRecord.getObject(name1)
                name2_Object = UserRecord.getObject(name2)
                if name2_Object.friends.search(name1) == True:
                    print ("    %s and %s are friends."%(name1, name2))    
                else:
                    print ("    %s and %s are not friends."%(name1, name2))
            
        elif command == "Exit":
            print ("    Exiting...")
            print ()
            break
            
        else:
            print ("Incorrect command in line %d, skip this line to the next line."%(num_line))
            
        print ()
        
    infile.close()
    
main()
