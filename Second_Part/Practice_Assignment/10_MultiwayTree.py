

class MultiwayTree:
    
    #given "pyTree", a Python representation of a tree, 
    #create node-and-pointer representation of that tree.
    def __init__(self,pyList):
        
        self.root = pyList[0]
        self.children =[]
        for child in pyList[1]:
            if child != []:
                self.children.append(MultiwayTree(child))
        
    #print out the node-and-pointer representation of a tree using preorder.   
    def preOrder(self): 
        print (self.root, end =' ')
        if self.children != []:
            for child in self.children:
                child.preOrder()
            
        
          
    #return True if the tree "self" has the same 
    #structure as the tree "other", "False" otherwise.
    def isIsomorphicTo(self,other):  
        if len(self.children) != len(other.children):
            return False
        else:
            for i in range(len(self.children)):
                if ( self.children[i] ).isIsomorphicTo( other.children[i] ) == False:
                    return False
            return True

def main():
    
    ############################ GET NUMBER OF LINE IN DOC ############################
    infile2 = open("10_MultiwayTreeInput.txt", "r")
    doc_len = 0
    for line in infile2:
        doc_len += 1   
    infile2.close()

    #print (doc_len)
    
    
    infile = open("10_MultiwayTreeInput.txt", "r")
    
    ########################### LOOP THROUGH LINE AND PROCESS ###########################
    tree_num = 0
    for i in range(int(doc_len/2)):
       
        ################################ FIRST TREE ################################
        line1 = ( infile.readline() ).strip()
        
        first_num = tree_num+1
        print ("Tree "+str(first_num)+":  "+line1)
        
        tree1 = MultiwayTree(eval(line1))
        
        
        print ("Tree "+str(first_num)+" preorder:   ", end = "" )
        tree1.preOrder()
        print ()
        print ()
        ################################ SECOND TREE ################################
        line2 = ( infile.readline() ).strip()
        
        second_num = tree_num+2
        print ("Tree "+str(second_num)+":  "+line2)
        
        tree2 = MultiwayTree(eval(line2))
        
        print ("Tree "+str(second_num)+" preorder:   ", end = "" )
        tree2.preOrder()
        print ()
        print ()
        ################################ isomorphic ################################
        
        if tree1.isIsomorphicTo(tree2):
            print ("Tree "+str(first_num)+" is isomorphic to Tree "+str(second_num)+"\n\n")
            
        else:
            print ("Tree "+str(first_num)+" is not isomorphic to Tree "+str(second_num)+"\n\n")
        
        tree_num += 2
    
           
    infile.close()
    
     
main()

