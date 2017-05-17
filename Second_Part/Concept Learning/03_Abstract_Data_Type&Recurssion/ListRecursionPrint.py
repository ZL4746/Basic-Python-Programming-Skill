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

class UnorderedList ():

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
         if current.getData() == item:
            found = True
         else:
            current = current.getNext()

      return found

   def remove (self,item):
      current = self.head
      previous = None
      found = False

      while not found:
         if current.getData() == item:
            found = True
         else:
            previous = current
            current = current.getNext()

      if previous == None:
         self.head = current.getNext()
      else:
         previous.setNext(current.getNext() )


def printList(myList):

   if not myList == None:
      print(myList.getData())
      printList(myList.getNext())


def main():

   myList = UnorderedList()
   myList.add("prosper")
   myList.add("and")
   myList.add("long")
   myList.add("Live")

   printList(myList.head)
   
main()
