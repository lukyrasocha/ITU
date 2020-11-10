def sayName():
	S = input()
	if len(S) >=1 and len(S) <=50 and not "  " in S and not " " in S[0] and not " " in S[-1] and all(x.isalpha() or x.isspace() for x in S):
		print("Thank you, " + S + ", and farewell!")
		
sayName()			