from bsddb3 import db 
#Get an instance of BerkeleyDB
def main():

	Runtime = True
	while Runtime:
		Dname = ""
		qList = []
		database = db.DB() 
		reviewDB = db.DB()
		reviewDB.open("rw.idx")

		user_input = input("Enter your queries here: ")
		if user_input.find(":") != -1:
			split_input = user_input.split(":")
			Dname = split_input[0]
			del split_input[0]
			split_input = split_input[0].split()
		elif user_input.find("rscore") != -1:
			Dname = "rs"
		else:
			split_input = user_input.split()



		if Dname == "p":
			database.open("pt.idx")
		elif Dname == "r":
			database.open("rt.idx")
		elif Dname == "rs":
			database.open("sc.idx")

		cur = database.cursor()
		rcur = reviewDB.cursor()

		for i in split_input:
			if Dname != "" :
				iter = cur.first()
				while iter:
					if iter[0].decode("utf-8") == i:
						if iter[1].decode("utf-8") not in qList:
							qList.append(iter[1].decode("utf-8"))
					iter = cur.next()
			elif Dname == "" :
				iter = rcur.first()
				while iter:
					if i in iter[1].decode("utf-8"):
						print(iter[0].decode("utf-8"))
					# if iter[0].decode("utf-8") in qList:


		rcur.close()
		cur.close()
		print(qList)
		if qList == []:
			print("Sorry we do not have any data on your queries.")
		iter = rcur.first()
		while iter:
			if iter[0].decode("utf-8") in qList:
				fOut = iter[1].decode("utf-8")
				fOut =fOut.replace(',', '')
				fOut = fOut.split('"')
				print("Product ID:",fOut[0])
				print("Product Name:",fOut[1])
				print("Product Price:",fOut[2])
				print("User Name:",fOut[3])
				print("Review Title:",fOut[5])
				print("Full Review:",fOut[7])
				print("*===============================*")
			iter = rcur.next()
		rcur.close()
		Termniate = input("Is that all? (T/F) :")
		if Termniate == "T":
			Runtime = False
		else:
			Runtime = True

	reviewDB.close()
	database.close()

if __name__ == "__main__":
    main()
