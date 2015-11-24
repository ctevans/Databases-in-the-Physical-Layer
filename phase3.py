from bsddb3 import db
import sys 
import string
import math
import re
#Get an instance of BerkeleyDB
def updateList(tList, uList, cNum):
        for x in tList:
                if tList.count(x) == cNum :
                        uList.append(x)
        uList = list(set(uList))
        return uList

def main():
        Runtime = True
        while Runtime:
                minPrice = 0
                maxPrice = float("inf")
                minRscore = 0
                maxRscore = float("inf")                
                priceCondition = False

                dateCondition = False
                tList = []
                uList = []
                Dname = ""
                qList = []
                database_pt = db.DB()
                database_rt = db.DB()
                database_sc = db.DB()
                reviewDB = db.DB()
                database_pt.open("pt.idx")
                database_rt.open("rt.idx")
                database_sc.open("sc.idx")
                reviewDB.open("rw.idx")
                split_input = []
                user_input = input("Enter your queries here: ")
                r_input = user_input.split()
                for i in range(len(r_input)):
                        
                        if r_input[i] == ">" or r_input[i] == "<":
                                r_input[i] = r_input[i-1] + r_input[i] + r_input[i+1]
                                r_input[i-1] = ""
                                r_input[i+1] = ""

                for i in r_input:
                        if i != "":
                                split_input.append(i)
                cNum = len(split_input)


                
                for i in range(len(split_input)):
                        
                        if "%" in split_input[i]:
                                split_input[i] = split_input[i].replace("%","*")

                for i in range(len(split_input)):
                        if split_input[i].find("pprice") != -1 :
                                split_input2 = []
                                priceCondition = True
                                for char in split_input[i]:
                                        if (char==">"):
                                                split_input2 = split_input[i].split(">")
                                                split_input2.append(split_input2[1])
                                                split_input2[1]=">"
                                        if (char=="<"):
                                                split_input2 = split_input[i].split("<")
                                                split_input2.append(split_input2[1])
                                                split_input2[1]="<"
                                
                                for item in split_input2:
                                        if ((item !="pprice") or (item !=">") or (item !="<")):
                                                price = item
                                                
                                if ((split_input2[0]=="pprice" and split_input2[1]==">") or (split_input2[2]=="pprice" and split_input[1]=="<")):
                                        minPrice = float(price)
                                else:
                                        maxPrice = float(price)
                                                                
                                
                        elif split_input[i].find(":") != -1 :
                                xplit = split_input[i].split(":")
                                Dname = xplit[0]
                                if Dname == "p":
                                        cur = database_pt.cursor()
                                elif Dname == "r":
                                        cur = database_rt.cursor()
                                del xplit[0]
                                iter = cur.first()
                                while iter:
                                        if iter[0].decode("utf-8") == xplit[0]:
                                                if iter[1].decode("utf-8") not in qList:
                                                        qList.append(iter[1].decode("utf-8"))
                                        iter = cur.next()
                                cur.close()

                        elif split_input[i].find(">") != -1 :
                                print(split_input[i])
                                xplit = split_input[i].split(">")
                                Dname = xplit[0]
                                if Dname == "rscore" :
                                        cur = database_sc.cursor()
                                        print(Dname)
                                del xplit[0]
                                iter = cur.first()
                                sscore = float(xplit[0])
                                while iter:
                                        cscore = iter[0].decode("utf-8")
                                        cscore = float(cscore)
                                        if cscore > sscore:
                                                if iter[1].decode("utf-8") not in qList:
                                                        qList.append(iter[1].decode("utf-8"))
                                        iter = cur.next()
                                cur.close()

                        elif split_input[i].find("*") != -1 :
                                cur = reviewDB.cursor()
                                iter = cur.first()
                                while iter:
                                        tDump = iter[1].decode("utf-8")
                                        if re.search(split_input[i],tDump):
                                                if iter[0].decode("utf-8") not in qList:
                                                        qList.append(iter[0].decode("utf-8"))
                                        iter = cur.next()
                                cur.close()

                        else:
                                cur = reviewDB.cursor()
                                iter = cur.first()
                                while iter:
                                        if split_input[i] in iter[1].decode("utf-8"):
                                                if iter[0].decode("utf-8") not in qList:
                                                        qList.append(iter[0].decode("utf-8"))
                                        iter = cur.next()

                        for t in qList :
                                tList.append(t)
                        qList = []
                uList = updateList(tList,uList,cNum)

                rcur = reviewDB.cursor()
                if uList == []:
                        print("Sorry we do not have any data on your queries.")
                iter = rcur.first()
                while iter:
                        
                        
                        if iter[0].decode("utf-8") in uList:
                                conditionsMet=True
                                fOut = iter[1].decode("utf-8")
                                fOut = fOut.split('"')
                                price =fOut[2].split(",")
                                price = price[1]
                                if ((priceCondition) and (price=="unknown" or (float(price) > maxPrice) or (float(price) < minPrice))):
                                        conditionsMet=False
                                print(conditionsMet)
                                if (conditionsMet):
                                        print("Product ID:",fOut[0].replace(',', ''))
                                        print("Product Name:",fOut[1].replace(',', ''))
                                        print("Product Price:",price)
                                        print("User Name:",fOut[3].replace(',', ''))
                                        print("Review Title:",fOut[5].replace(',', ''))
                                        print("Full Review:",fOut[7].replace(',', ''))
                                        print("*===============================*")
                        iter = rcur.next()
                rcur.close()

        #       if user_input.find(":") != -1:
        #               split_input = user_input.split(":")
        #               Dname = split_input[0]
        #               del split_input[0]
        #               split_input = split_input[0].split()
        #       elif user_input.find("rscore") != -1:
        #               Dname = "rs"
        #       else:
        #               split_input = user_input.split()




        #       rcur = reviewDB.cursor()

        #       for i in split_input:
        #               if "%" in i:
        #                       i = i.replace("%","*")
        #               if Dname != "" :
        #                       iter = cur.first()
        #                       while iter:
        #                               if iter[0].decode("utf-8") == i:
        #                                       if iter[1].decode("utf-8") not in qList:
        #                                               qList.append(iter[1].decode("utf-8"))
        #                               iter = cur.next()
        #               elif Dname == "" :
        #                       iter = cur.first()
        #                       while iter:
        #                               tDump = iter[1].decode("utf-8")
        #                               if re.search(i,tDump):
        #                                       if iter[0].decode("utf-8") not in qList:
        #                                               qList.append(iter[0].decode("utf-8"))
        #                               iter = cur.next()




        #       rcur.close()
        #       cur.close()
                Termniate = input("Is that all? (T/F) :")
                if Termniate == "T":
                        Runtime = False
                else:
                        Runtime = True
        database_pt.close()
        database_rt.close()
        database_sc.close()
        reviewDB.close()


if __name__ == "__main__":
        main()
