
from copy import deepcopy


class State:

    ##########################INIT METHOD############################
    
    def __init__(self, grid, start_row, start_col, end_row, end_col, targetValue, path_history, sum_so_far):
        self.grid = grid
        self.start_row = start_row
        self.start_col = start_col
        self.end_row = end_row
        self.end_col = end_col
        self.targetValue = targetValue
        self.path_history = path_history
        self.sum = sum_so_far
    
    ##########################STRING METHOD THAT PRITNT THE CURRENT PROGRESS###########################
    
    def __str__(self):
        
        ##################METHOD TO PRINT THE GRID#####################
        outstring = "   Grid:"
        for i in range(len(self.grid)):
            line = "      "
            for j in range(len(self.grid[i])):
                if self.grid[i][j] != None:
                    line += "%-5d"%(self.grid[i][j])
                else:
                    line += "%-5s"%("None")
            outstring += "\n"+line
            
        ##################METHOD TO PRINT HISTORY, START POINT, SUM SO FAR#####################    
        outstring += "\n" + "   history: "+str(self.path_history)
        outstring += "\n" + "   start point: (%d,%d)"%(self.start_row, self.start_col)
        outstring += "\n" + "   sum so far: %d\n"%(self.sum)
        
        return (outstring)
        
 
 
 
 
 
 
 
        
        
def isValid (grid,row,column):
    
    ############################GET THE SIZE OF THE GRID#######################################
    size_row = len(grid)
    size_col = len(grid[0])
    
    ############################POINT OUTSIDE THE GRID#########################################
    if ( (row+1) > size_row ) or ( row < 0 ) or ( (column+1) > size_col ) or ( column < 0 ):
        return False
        
    #############################POINT THAT ALREADY TRIED######################################
    elif grid[row][column] == None:
        return False
        
    #############################POINT THAT HAVEN'T TRIED######################################
    else:
        return True



        
def solve(thisState):
    
    #############################CURRENT GRID STATUS##############################
    current_grid = thisState.grid
    current_row = thisState.start_row
    current_col = thisState.start_col

    current_targetValue = thisState.targetValue
    current_history = thisState.path_history
    current_sum = thisState.sum
    
    #############################GOLD STATE######################################
    print ("Is this a goal state?")
    if current_sum == current_targetValue:
        print ("Solution found!")
        return current_history
    
    #############################NOT GOLD######################################
    
    else:
        
        #############################SUM EXCEED TARGET SUM######################################
        ##################################BACK TRACK!!!#########################################
        
        if current_sum > current_targetValue:
            print ("No. Target exceeded:  abandoning path")
            
            #print (str(thisState))
            return None
        
        
        #############################MOVING RIGHT#####################################
        print ("No.  Can I move right?")
        if isValid(current_grid, current_row, current_col+1):
            print ("Yes!")
            print()
            newState = deepcopy(thisState)
            newState.start_col += 1
            
            new_point = newState.grid[newState.start_row][newState.start_col]
            newState.path_history.append(new_point)
            newState.sum += new_point
            
            newState.grid[newState.start_row][newState.start_col] = None
            
            print ("Problem is now:")
            print (str(newState))
            
            result = solve (newState)
            if result != None:
                return result
               
        #############################MOVING UP########################################     
        print ("No.  Can I move up?")     
        if isValid(current_grid, (current_row-1), current_col):
            print ("Yes!")
            print()
            newState = deepcopy(thisState)
            newState.start_row -= 1
            
            new_point = newState.grid[newState.start_row][newState.start_col]
            newState.path_history.append(new_point)
            newState.sum += new_point
            
            newState.grid[newState.start_row][newState.start_col] = None
            print ("Problem is now:")
            print (str(newState))
            
            result = solve (newState)
            if result != None:
                return result
        
        #############################MOVING DOWN######################################
        print ("No.  Can I move down?")
        if isValid(current_grid, (current_row+1), current_col):
            print ("Yes!")
            print()
            newState = deepcopy(thisState)
            newState.start_row += 1
            
            new_point = newState.grid[newState.start_row][newState.start_col]
            newState.path_history.append(new_point)
            newState.sum += new_point
            
            newState.grid[newState.start_row][newState.start_col] = None
            print ("Problem is now:")
            print (str(newState))
            
            result = solve (newState)
            if result != None:
                return result
        
        #############################MOVING LEFT######################################           
        print ("No.  Can I move left?") 
        #moving left
        if isValid(current_grid, current_row, current_col-1):
            print ("Yes!")
            print()
            newState = deepcopy(thisState)
            newState.start_col -= 1
            
            new_point = newState.grid[newState.start_row][newState.start_col]
            newState.path_history.append(new_point)
            newState.sum += new_point
            
            newState.grid[newState.start_row][newState.start_col] = None
            print ("Problem is now:")
            print (str(newState))
            
            result = solve (newState)
            if result != None:
                return result

        #############################CHECK AGAIN IF SUM EXCEED########################
        if current_sum > current_targetValue:
            print ("No. Target exceeded:  abandoning path")
            
            #print (str(thisState))
            return None
        
        #############################CANNOT MOVE ANY WAY##############################
        ################################BACK TRACK!!!#################################
        else:
            print ("Couldn't move in any direction.  Backtracking.")
    
            #print (str(thisState))
            return None
            
        
        
    
def main():
    
    #################################################################
    ############################OPEN FILE############################
    #################################################################
    
    
    infile = open("08_pathdata1.txt", "r")
    
    
    
    ##############################################################################
    ############################READ IN THE FIRST LINE############################
    ##############################################################################
    
    
    instruction_Line = infile.readline()
    instruction_Line = instruction_Line.strip()
    instruction_List = instruction_Line.split(" ")
    
    targetValue = int(instruction_List[0])
    grid_rows = int(instruction_List[1])
    grid_cols = int(instruction_List[2])
    start_row = int(instruction_List[3])
    start_col = int(instruction_List[4])
    last_row = int(instruction_List[5])
    last_col = int(instruction_List[6])
    
    
    #######################################################################
    ############################CREATE THE GRID############################
    #######################################################################
    
    
    #print (targetValue, grid_rows, grid_cols, start_row, start_col, end_row, end_col )
    
    grid = []
    for line in infile:
        line = line.strip()
        line_list = line.split(" ")
        line_list2 = []
        for item in line_list:
            line_list2.append(int(item))
        grid.append(line_list2)
    infile.close()
    #lastpoint = grid[last_row][last_col]  
    #print (grid)
    
    
    
    #########################################################################################
    ############################CREATE THE INITIAL STATE INSTANCE############################
    #########################################################################################
    
    path_history = []
    sum_so_far = 0
    thisState = State(grid, start_row, start_col, start_row, start_col, targetValue, path_history, sum_so_far)
    
    
    #########################################################################################
    ############################REACH THE START POINT IN THE GRID############################
    #########################################################################################
    
    
    #target the initial start point
    start_value = thisState.grid[thisState.start_row][thisState.start_col]
    thisState.path_history.append(start_value)
    thisState.sum += start_value
    thisState.grid[thisState.start_row][thisState.start_col] = None
    print (str(thisState))
    
    
    #########################################################################################
    ############################RECURSIVELY SOLVE THE MAZE###################################
    #########################################################################################
    
    result = solve(thisState)    
    
    if result == None:
        print ("No solution exists")
    else:
        print (result)
        
    #print ("The out point shoule be (%d,%d) in the grid, which is %d"%(last_row,last_col,lastpoint) )
    
main()