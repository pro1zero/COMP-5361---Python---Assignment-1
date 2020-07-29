# N is the number of propositional variables in terms of a string

N = input("Please enter the number of variables: ")
n = int(N)

#we cast the string N to integer n
truthvalues = []

for x in range(1,n+1):
	t = input("Enter truth value: ")
	truthvalues.append(t)
#we input the truth values of the variables in terms of 0 and 1
#print(truthvalues)

e = "((P ∧ Q) ∨ (R ∧ True) ∨ ((¬P ∧ ¬R) ∧ Q)"
m = e


for x in e:
	if(x=="∧"):
		e = e.replace("∧", "&")
	if(x==" "):
		e = e.replace(" ", "")
	if(x=="∨"): 
		e = e.replace("∨", "|")
	if(x=="¬"):
		e = e.replace("¬", "~")
	if(x=="→"):
		e = e.replace("→", "<")
	if(x=="⟺"):
		e = e.replace("⟺", ">")

e = e.replace("True", "1")
e = e.replace("False", "1")

#the above code strips the extra space and converts the and, or, implies and iff symbols to machine readable format
#print("updated" + e)

variables = ""


for x in e:
	if(x!='(' and x!=')' and x!='1' and x!='0' and x!='&' and x!='|' and x!='~' and x!='<' and x!='>'):
		if(x in variables):
			continue
		else:
			variables += x		

# the variable, (variables) gets the distinct propositional variable from the expression sentence string.
#print(variables)

for x in variables:
	for y in e:
		if(y=='P'):
			e = e.replace('P', truthvalues[0])
		if(y=='Q'):
			e = e.replace('Q', truthvalues[1])
		if(y=='R'):
			e = e.replace('R', truthvalues[2])

e = e.replace("~1", "0")
e = e.replace("~0", "1")

#print(e)

# we then convert the True and False to 1 and 0 respectively and we remove the not(~) symbol by taking the complement of the current symbol

stack = []
parentheses = []
operators = []

def operation(t1, t2, t3):
	if(t2 == '&'):
		return int(t1) and int(t3)
	if(t2 == '|'):
		return int(t1) or int(t3)
	if(t2 == '<'):
		return not int(t1) or int(t3)
	if(t2 == '>'):
		return ((not int(t1) or int(t3)) and (not int(t3) or int(t1)))
# the function operations is for the basic operations and, or, implication and if and only if function.
res = 0

for x in e:
	if x == ' ':
		continue
	if x == '(':
		parentheses.append(x)

	if x == '1' or x == '0':
		stack.append(x)
	
	if x == '&' or x == '|' or x == '<' or x == '>':
		operators.append(x)

	if x == ')':
		value2 = stack.pop()
		value1 = stack.pop()
		ope = operators.pop()
		result = operation(value1, ope, value2)
		stack.append(result)
		parentheses.pop()

while(len(operators) != 0):
	if(len(stack) >= 2 and len(operators) >= 1):
		value2 = stack.pop()
		value1 = stack.pop()
		ope = operators.pop()
		result = operation(value1, ope, value2)
		stack.append(result)
		#parentheses.pop()


# the above is the stack implementation of the code which takes the parentheses in the parentheses stack, operators in the operators stack and values 1 and 0 in the stack named "stack"


pin = stack.pop()

#pin is the top element of the stack-------->pin = stack[-1]

if(pin == 0):
	print("Truth Value of " + m  + ": False" )
else:
	print("Truth Value of " + m  + ": True" )
	
#coded by jenish soni (40132415)