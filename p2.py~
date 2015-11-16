#Open the file and only have it so that it is being read.
f = open('10.txt', "r")
o = open('reviews.txt', "w")


#Read in the file line by line!
line  = True
counter = 1
counterChange = True




print(counter,end="")
o.write(str(counter))
#print(",",end="") # That initial 1 
#series of while loops that parse the input a metric ton.
while line:
    line = f.readline()
    line.strip('\n') 
    splittingFunction = line.split(": ",1)

    
    #PUT IN A " FOR THE SELECTED OPTION
    if (splittingFunction[0] == "review/text") or (splittingFunction[0] == "product/title") or(splittingFunction[0] == "review/summary") or (splittingFunction[0] == "review/profileName"):
        print("\"",end="")
        o.write("\"")




    print(splittingFunction[-1].strip('\n'),end="")
    o.write(splittingFunction[-1].strip('\n'))

    if line == "\n":
        print()
        counter = counter +1
        print(counter,end="")
        o.write(str(counter))

    if (splittingFunction[0] == "review/text") or (splittingFunction[0] == "product/title") or(splittingFunction[0] == "review/summary") or (splittingFunction[0] == "review/profileName"):
        print("\"",end="")
        o.write("\"")
    print(",", end="")
    o.write(",")
        

f.close()
