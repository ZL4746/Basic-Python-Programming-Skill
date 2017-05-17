class Stack():
#   
#  Stack methods as defined in class
#
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

############################################################################

def postfixEval(postfixExpr):

   operandStack = Stack()

   tokenList = postfixExpr.split()

   for token in tokenList:
      if token in "/*+-":
          
         #  Found an operator:  pop two operands from the stack,
         #     do the operation, and then push the result on the stack
         operand2 = operandStack.pop()
         operand1 = operandStack.pop()
         result = doMath(token,operand1,operand2)
         operandStack.push(result)
         print("found operator '"+token+"': popping",operand2,"and",operand1)
         input("paused")
         print("pushing",operand2,token,operand1,"   stack now: ",operandStack)
         input("paused")
      else:
         #  Found an operand:  push it on the stack         
         operandStack.push(int(token))
         print("pushing",token,"   stack now: ",operandStack)
         input("paused")         

   return operandStack.pop()

def doMath(op,op1,op2):
#
#  Applies operator "op" to operands "op1" and "op2"
#
   if op == "*":
      return op1 * op2
   elif op == "/":
      return op1 / op2
   elif op == "+":
      return op1 + op2
   else:
      return op1 - op2

def main():

   problem = "7 13 + 3 2 * +"
   print("Evaluate: ",problem)
   answer = postfixEval(problem)
   print("Final answer: ",answer)

main()
