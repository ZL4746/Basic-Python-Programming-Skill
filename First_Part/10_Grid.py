def main():
      
      #open the file
      infile = open("grid.txt", "r")
      
      #read the dimenstion of the grid
      dim = infile.readline()
      dim = dim.strip()
      dim = int(dim)
      
      #create an empty grid
      grid = []
      
      #populate the grid
      for i in range (dim):
            row = infile.readline()
            row = row.strip()
            row = row.split()
            for j in range (dim):
                  row[j] = int(row[j])
            grid.append(row)
            
      #print(grid)
      
      #close the file
      infile.close()
      
      #initialize a list to record the max product for each situation
      max_products = []
      
      #1. 
      #read each row in block of four, 
      #and get the greast product for row process
      row_max = 0
      for row in grid:
            for i in range(0, dim-3):
                  product = 1
                  for j in range(i,i+4):       
                        product *= row[j]    
                  if product > row_max:
                        row_max = product
      
      #print ("row_max = ", row_max) 
      max_products.append(row_max)                        
                          
      #2.
      #read each column in block of four, 
      #and get the greatest product for column process
      col_max = 0
      for j in range(dim):
            for i in range(0, dim-3):
                  product = 1
                  for k in range(i, i+4):
                        product *= grid[k][j]
                  if product > col_max:
                        col_max = product
                        
      #print ("col_max = ", col_max)                  
      max_products.append(col_max)    
       
      #3.
      #read along diagonal row by row from L to R in block of 4, 
      #and get the greatest product for diagonal process
      '''
      for i in range(dim-3):
            for j in range(dim - 3):
                  for k in range(4):
                        print(grid[i+k][j+k], end=" ")
                  print(end= " ")
            print() 
      '''
      dia_max = 0
      for i in range(dim-3):
            for j in range(dim - 3):
                  product = 1
                  for k in range(4):
                        product *= grid[i+k][j+k]
                  if product > dia_max:
                        dia_max = product
      #print ("dia_max = ", dia_max)
      max_products.append(dia_max)
         
      #4.
      #read along diagonal row by row from R to L in block of 4, 
      #and get the greatest product for diagonal process
      '''
      for i in range(0, dim - 3):
            for j in range(3, dim):
                  
                  for k in range(4):
                         
                        print(grid[i + k][j - k], end=" ")
                  print(end=" ")
      '''
      dia_max2 = 0 
      for i in range(0, dim - 3):
            for j in range(3, dim):
                  product = 1
                  for k in range(4):
                        product *= grid[i + k][j - k]
                  if product > dia_max2:
                        dia_max2 = product
                              
      #print ("dia_max2 = ", dia_max2)
      max_products.append(dia_max2)
      
      
      #5. Get the max product from the max product List
      #print (max_products)
      maxProduct = max(max_products)
      
      #Printing statement for the output
      print ("The greatest product is %d."%(maxProduct))
      
main()