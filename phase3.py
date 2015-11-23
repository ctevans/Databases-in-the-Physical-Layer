from bsddb3 import db
import re
#Get an instance of BerkeleyDB
def main():
        Runtime = True
        while Runtime:
                Dname = ""
                qList = []
                database = db.DB() 	       
                reviewDB = db.DB()
                reviewDB.open("rw.idx")
                user_input = input("Enter your queries (or type 'quit' to quit):")
                if user_input.lower() == 'quit':
                        Runtime = False
                        print("Goodbye")
                        return
                elif user_input.find(":") != -1:
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
                else:
                        database.open("rw.idx")

                cur = database.cursor()
                rcur = reviewDB.cursor()

                for i in split_input:
                        if "%" in i:
                                print(i)
                                i = i.replace("%","??")
                        print(i)
                        if Dname != "" :
                                iter = cur.first()
                                while iter:
                                        if iter[0].decode("utf-8") == i:
                                                if iter[1].decode("utf-8") not in qList:
                                                        qList.append(iter[1].decode("utf-8"))
                                        iter = cur.next()
                        elif Dname == "" :
                                iter = cur.first()
                                while iter:
                                        if i in iter[1].decode("utf-8"):
                                                if iter[0].decode("utf-8") not in qList:
                                                        qList.append(iter[0].decode("utf-8"))
                                        iter = cur.next()


                rcur.close()
                cur.close()
                rcur = reviewDB.cursor()
                if qList == []:
                        print("Sorry we do not have any data on your queries.")
                iter = rcur.first()
                while iter:
                        if iter[0].decode("utf-8") in qList:
                                fOut = iter[1].decode("utf-8")
                                fOut = fOut.split('"')
                                price =fOut[2].split(",")
                                price = price[1]
                                print("Product ID:",fOut[0].replace(',', ''))
                                print("Product Name:",fOut[1].replace(',', ''))
                                print("Product Price:",price)
                                print("User Name:",fOut[3].replace(',', ''))
                                print("Review Title:",fOut[5].replace(',', ''))
                                print("Full Review:",fOut[7].replace(',', ''))
                                print("*===============================*")
                        iter = rcur.next()
                rcur.close()

        reviewDB.close()
        database.close()

if __name__ == "__main__":
        main()
