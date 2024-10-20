#function to define the operations
def precedence(op):
    if op == "+" or op=="-":
        return 1
    if op== "*" or op=="/":
        return 2 
    if op == "^":
        return 3 
    return 0

#Function to check if the character is an alphabet or number 
def is_operand(ch):
    return ch.isalnum() #identifies if its a number or alphabet 

#function to convert infix expression to ppostfix 
def infix_to_postfix(expression):
    #stack for storing operators 
    stack = []
    #result of postfix expression 
    postfix = []


    #iterate through the expression 
    for char in expression:
        #if the character is an number or letter than add it to the postfix stack
        if is_operand(char):
            postfix.append(char)
        #if the character is "(" put it into the stack 
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(": # ! = means NOT EQUAL 
                postfix.append(stack.pop())
            stack.pop() #pop the "(" from the stack 
            #if the character is an operator 
        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                postfix.append(stack.pop())
            stack.append(char)

    #pop all remaining operators in the stack 
    while stack:
        postfix.append(stack.pop())

    #join the list to form the postfix expression 
    return " ".join(postfix)
    
    #example 
expression = "A+B(C^D-E)"
print("infix expression:",expression)
print("postfix expression:", infix_to_postfix(expression))









