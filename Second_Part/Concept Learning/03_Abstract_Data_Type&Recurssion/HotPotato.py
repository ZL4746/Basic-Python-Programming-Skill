import random

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


def hotPotato(namelist,num):

   simqueue = Queue()

   for name in namelist:
      simqueue.enqueue(name)

   while simqueue.size() > 1:
      for i in range(num-1):
         simqueue.enqueue(simqueue.dequeue())

      print("Deleting",simqueue.peek())
      pause = input("pausing. . .")
      simqueue.dequeue()

   return simqueue.dequeue()


def main():

   romans = ["Thomas","Daniel","Anthony","Bill","Mohammad","David","Casey"]
#   random.shuffle(romans)
   print(romans)

   pause = input("pausing. . .")
   survivor = hotPotato(romans, 7)
   print("Survivor is: ",survivor)

main()
