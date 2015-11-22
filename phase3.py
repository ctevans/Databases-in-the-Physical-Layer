from bsddb3 import db 
#Get an instance of BerkeleyDB
Runtime = True
while Runtime:
	database = db.DB() 
	user_input = input("Enter your queries here:")
	if user_input.find(":") != -1:
		split_input = user_input.split(":")
		Dname = split_input[0]
		del split_input[0]
	else:
		split_input = user_input.split()
	print(Dname,split_input)
	database.open("sc.idx")
	cur = database.cursor()
	iter = cur.first()
	while iter:
	 print(iter)
	 iter = cur.next()
	cur.close()
	Termniate = input("Is that all? (T/F) :")
	if Termniate == "T":
		Runtime = False
	else:
		Runtime = True
	database.close()
