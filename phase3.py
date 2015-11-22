from bsddb3 import db 
#Get an instance of BerkeleyDB
Runtime = True
while Runtime:
	Dname = ""
	database = db.DB() 
	user_input = input("Enter your queries here:")
	if user_input.find(":") != -1:
		split_input = user_input.split(":")
		Dname = split_input[0]
		del split_input[0]
		split_input = split_input[0].split()
	else:
		split_input = user_input.split()
		atabase.open("rw.idx")
	print(split_input)
	if Dname :
		if Dname == "p":
			database.open("pt.idx")
		elif Dname == "r":
			database.open("rt.idx")
	cur = database.cursor()
	iter = cur.first()
	while iter:
		if iter[0].decode("utf-8") == "art":
			print(iter)
		iter = cur.next()
	cur.close()
	Termniate = input("Is that all? (T/F) :")
	if Termniate == "T":
		Runtime = False
	else:
		Runtime = True
	database.close()
