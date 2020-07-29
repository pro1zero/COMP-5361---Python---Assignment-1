#initialising variables to 0 for the count of truth values 

taut = 0
contra = 0

print("====================================================================================================================================================================")
print("     P1    |     P2     |      ~P1   |    P1 V P2   |    S(Output)")
print()

for P1 in [True,False]:
	for P2 in [True, False]:
		S = (not(not P1 and (P1 or P2)) or P2)
		if S==True: 
			taut = taut + 1

		else:
			contra = contra + 1


		print("   " ,P1, "    |   " ,P2, "   |   "  ,not P1, "   |   " ,P1 or P2, "   |   " ,S)

if taut == 4:
	print("S is a TAUTOLOGY")
elif contra == 4:
	print("S is a CONTRADICTION")
else:
	print("S is a CONTINGENCY")
# as there are only 2 propositional variables here, the maximum values as true and false can be 4 (2^2 = 4)
print("====================================================================================================================================================================")

taut = 0
contra = 0
# again changing their values to zeroes

print("      P1     |      P2     |     ~P1     |    ~P2   |     P1=>~P2   |   ~P1=>~P2  |  S(Output)  ")
print()

for P1 in [True,False]:
	for P2 in [True, False]:
		S = P2 and (not P1 or not P2) and (P1 or not P2)
		if S==True: 
			taut = taut + 1

		else:
			contra = contra + 1


		print("   " ,P1, "    |   " ,P2, "   |   "  ,not P1, "   |   " ,not P2, "   |   " ,not P1 or not P2, "   |   " ,P1 or not P2, "   |   " ,S)


if taut == 4:
	print("S is a TAUTOLOGY")
elif contra == 4:
	print("S is a CONTRADICTION")
else:
	print("S is a CONTINGENCY")

# as there are only 2 propositional variables here, the maximum values as true and false can be 4 (2^2 = 4)


print("====================================================================================================================================================================")
# again changing their values to zeroes
taut = 0
contra = 0

print("       P1    |     P2     |    P3    |     ~P1     |      ~P2      |     ~P3     |    P2=>P3  |P1=>(P2=>P3)|   P1=>P2   | P1=>(P2=>P3) |  S(Output)")
print()

for P1 in [True,False]:
	for P2 in [True, False]:
		for P3 in [True, False]:

			S = (P1 and P2 and not P3) or ((P1 and not P2) or P3)
			if S==True: 
				taut = taut + 1

			else:
				contra = contra + 1


			print("   " ,P1, "    |   " ,P2, "   |   "  ,P3, "   |   " ,not P1, "   |   " ,not P2, "   |   " ,not P3, "   |   " ,not P2 or P3, "   |   " ,not P1 or(not P2 or P3), "   |   " ,not P1 or P2, "   |   " ,not P1 or (not P2 or P3), "   |   " ,S)


if taut == 8:
	print("S is a TAUTOLOGY")
elif contra == 8:
	print("S is a CONTRADICTION")
else:
	print("S is a CONTINGENCY")

# as there are 3 propositional variables here, the maximum values as true and false can be 8 (2^3 = 8)
# coded by jenish soni