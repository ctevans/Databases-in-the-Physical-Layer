from collections import Counter
import collections
import re

#Open the file and only have it so that it is being read.
f = open('1k.txt', "r")

#Now here are all of the files we will be writing to.
#This one is the main big file we will write to.
o = open('reviewstemp.txt', "w")

#These are the smaller files we will write to.
scoreTextFile = open('scores.txt', 'w')
rtermsTextFile = open('rterms.txt', 'w')
ptermsTextFile = open('pterms.txt', 'w')


#FILE PROCESSING BEGINS HERE!
#Read in the file line by line!
line  = True
counter = 1
counterChange = True
noCommaFlag = False

titleWordFreqDict = collections.OrderedDict()
termWordFreqDict = collections.OrderedDict()


o.write(str(counter))
o.write(",")
#series of while loops that parse the input a metric ton.
while line:
    line = f.readline()

    line.strip('\n') 
    splittingFunction = line.split(": ",1)

    
    #PUT IN A " FOR THE SELECTED OPTION
    if (splittingFunction[0] == "review/text") or (splittingFunction[0] == "product/title") or(splittingFunction[0] == "review/summary") or (splittingFunction[0] == "review/profileName"):

        o.write("\"")



#####################
#This block deals with  TITLE OF PRODUCT
######################
    if splittingFunction[0] =="product/title":
        titleSplitString = splittingFunction[1].split()
        for word in titleSplitString:
            
            word = word.lower()

            word = "".join([c if c.isalnum() else " " for c in word])
            wordSplit = word.split()
            for wordy in wordSplit:
                if len(wordy) > 2:
                    termsSplitString = splittingFunction[1].strip('\n')
                    ptermsTextFile.write(wordy)
                    ptermsTextFile.write(",")
                    ptermsTextFile.write(str(counter) + "\n") 


#####################
#This block deals with  TITLE OF PRODUCT
######################
#####################
#This block deals with RTERMS.TXT
######################

    
    removeTheseChars = ["\\", "/", "|", "-", "_", "(", ")", "[", "]", "{", "}", "!", "?", "*", "%", "$", "#", "@", "~", "`", ".", ",", ":", ";", "^", "$", "@", "'s"]
    if (splittingFunction[0] =="review/summary") or (splittingFunction[0] == "review/text"):
        termsSplitString = splittingFunction[1].split()
        for word in termsSplitString:
            word = word.lower()
            
            for character in removeTheseChars:
                word = word.replace(character, " ")
            wordySplit = word.split()
            for word in wordySplit:
                word = "".join([c if c.isalnum() else "" for c in word])
                if len(word) > 2:  
                    
                    termsSplitString = splittingFunction[1].strip('\n')
                    word = word.replace("quot", "")
                    rtermsTextFile.write(word)
                    rtermsTextFile.write(",")
                    rtermsTextFile.write(str(counter) + "\n")






#####################
#END block deals with RTERMS.TXT
######################
#####################
#This block deals with SCORES.TXT STORAGE OF DATA!
######################

    

    if splittingFunction[0] == "review/score":
        scoreSplitString = splittingFunction[1].strip('\n')


        scoreTextFile.write(scoreSplitString)
        scoreTextFile.write(",")
        scoreTextFile.write(str(counter) + "\n")
    
        
  
#####################
#END block deals with SCORES.TXT STORAGE OF DATA!
######################


    firstModString = splittingFunction[-1].strip('\n')
    firstModStringModifiedAgain = firstModString.replace("\"", "&quot;") 
    o.write(firstModStringModifiedAgain)

    if line == "\n":

        o.write("\n")
        counter = counter +1

        o.write(str(counter))
        noCommaFlag = True


    if (splittingFunction[0] == "review/text"):
        continue
    

    if (splittingFunction[0] == "review/text") or (splittingFunction[0] == "product/title") or(splittingFunction[0] == "review/summary") or (splittingFunction[0] == "review/profileName"):

        o.write("\"")


    #if (noCommaFlag != True):


    o.write(",")
    #    noCommaFlag = False
    #noCommaFlag = False
        

f.close()
o.close()
scoreTextFile.close()

#At this point we have a temporary file made, this is nice. But it is not 
#enough. Now I take that temporary file and remove that disgusting last line
#of mess. I just despise it.
#I put this in the final reviews file to be used.

reviewsTemp = open('reviewstemp.txt', "r")
reviewsFile = open('reviews.txt', "w")

lines2 = True

while lines2:
    lines2 = reviewsTemp.readline()
    if lines2.split(',')[-1]:
        lines2string = str(lines2)
        lines2stringmod = lines2string.replace('\\', '\\\\')
        lines2stringmod2 = lines2stringmod.replace("\n", "\"\n")

        #Write to the file this new modified string
        reviewsFile.write(lines2stringmod2)

    
reviewsTemp.close()
reviewsFile.close()
    
rtermsTextFile.close()
ptermsTextFile.close()
print("SUCCESS! And we processed this many reviews!!!! :)", counter-1)





