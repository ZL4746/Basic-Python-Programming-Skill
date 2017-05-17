import math
import random

def computePI (n):
      
      #initialize the count to count how many times the point is inside the circle
      count_inside = 0
      
      #use a loop to stimulate the test
      for i in range(1, n+1):  
            
            #generate random point inside the dart board
            xPos = random.uniform (-1.0, 1.0)
            yPos = random.uniform (-1.0, 1.0) 
            distance_from_center = math.hypot (xPos, yPos)
            
            #compare the distance from center to the radius
            #increase count if it is inside the circle
            if (distance_from_center < 1):
                  count_inside += 1
      
      #calculate the computed_pi after the stimulation      
      computed_pi = (count_inside / n)*4
      
      return computed_pi

def main ():
      
  print ()
  print ("Computation of PI using Random Numbers")
  print ()
  
  #use the while loop to input the tested value repeatedly
  
  numThrows = 100
  while numThrows <= 10000000:
        
        #get the computed pi from the stimulation
        computed_pi = computePI ( numThrows )

        #determine the difference between the computed pi and the real pi
        difference = computed_pi - math.pi

        #use string formatted for display purpose, and print them
        print ("num = %d\t"%(numThrows) + "Calculated PI = %.6f"%(computed_pi) + "  Difference = " + "{:+.6f}".format(difference))
            
        numThrows *= 10     
               

  print ()
  print ("Difference = Calculated PI - math.pi")
  print ()

main()