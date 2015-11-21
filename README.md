# Databases-in-the-Physical-Layer
The goal of this project is to teach the concept of working with data in the physical layer. This is done by building an information retrieval system, using the Berkeley DB library for operating on files and indices. Your job in this project is to write programs that keep data in files and maintain indices that provide basic searches over data. 


#### "Shhhh Just tell me how to use it so I can get started!"
Here is how to get started:
Type in the following commands in order in the terminal:

1: chmod 755 justDoIt (incase it isn't executable yet)
2: ./justDoIt

Boom. Part 1 and part 2 done.
Now you have the 4 files to begin processing.

Want to clean the directory of all of the produced files and leave only core essential files and tester files?

1: chmod 755 cleaningScript (incase it isn't executable yet)
2: ./cleaningScript

Want to actually see what is present in the database files ("index files")?

1: chmod 755 showWhatIsInDatabase
2: ./showWhatIsInDatabase

This will produce four files that will contain in themselves the full contents of the databases. Makes it simpler to check. Could even run diff on it if you wanted. These files should look the exact same as the input prettymuch.

IE:
*Some misc database specification information here*

 key1
 
 value1
 
 key2
 
 value2
 
 key3
 
 value3
 
 key4
 
 value4
 
...

The file names are as follows:

dbDumpFilerw

dbDumpFilert

dbDumpFilept

dbDumpFilesc

Now everything is ready for phase 3. 



####This project is divided into three phases.

    Phase 1: Parsing of a large volume of reviews.

    Phase 2: Loading parsed files into a database.

    Phase 3: Creating a query program / structure to access the database.


Files of note:

    [PYTHON] p2.py: Parses a given bulk file of reviews in depth. Produces 4 heavily parsed text files.
    
    [SCRIPT] thisIsTheSortCommand: Sorts and removes duplicates within files produced by p2.py and maintains original file names.
    
    [PYTHON] loadIntoDatabase.py: The file that takes the sorted files from thisIsTheSortCommand and puts them into the database.
    
    [SCRIPT] dbLoadScript: Will run through the python3 program dbLoadChangeFileFormat.py and prep files. Will then take each of
             these prepared files and will put them into the database indexes we desire using db_load.
             
    [PYTHON] dbLoadChangeFileFormat: Will take in a text file after being processed and will modify the format to be acceptable
             to be used with the db_load command. 
             
    [SCRIPT] cleaningScript: Our directory can become a mess after running everything. So how should this be solved? Making a
             fairly straightforward easy-to-use method that will remove ANYTHING that I've seen be made before from the directory.
             
    [SCRIPT] showWhatIsInDatabases: This is going to be a useful script for testing. We cannot simply use VIM or emacs to open up
             the database. So what I have here is an easy-to-use user-friendly script that will dump all of the data currently
             present within our indexes into four seperate files. This makes it easy to open in one's fave text editor and check
             for consistency. 
             
    [SCRIPT] justDoIt: As Shia LeBeouf said... just do it!
             What this script will do is it will just connect all of these files together and dodge the hilarious irritation of trying
             to string all these various commands together. No! NO! Instead you can just run this command in the terminal and then in
             doing so you actually just produced the 4 index files and only typed in a single line! 

Languages used:

    Python 3.X: Carried the bulk of the workload in this project.
    
    Shell Script: Used to provide a gentle and easy-to-use way to provide a bridge between python programs
    
    

### Phase #1: Parsing
Language: Python 3.x
File associated with this: p2.py


Given a huge dump of reviews... let's parse it into something that we can later load into a database and actually make use of.
This is written in python version 3.x, to run it I typically just called it on the commandline. Below are some specifications of what this program needs to take in and what it will produce.
*Please refer to the sample inputs and outputs on the wiki if you are interested in specific examples!

#####Input:

*Give it some sort of input file. (For now I have this hard coded, I may make it more flexible later.



#####Output: This file will CREATE the following files:

    reviews.txt

    pterms.txt

    rterms.txt

    scores.txt


### Phase #2: Loading into our database 
### (But before that... the ever essential sorting!)

#### Sorting and removal of duplicates
Language: Shell scripting
File associated with this: thisIsTheSortCommand


Let's suppose for a second that we want to sort these files. Instead of making my own sort (I could happily write mergesort!) I am going to instead utilize the linux sort command here. Proven, stable, effective method. (Of course this now means this must be run on a linux system- perhaps in the future a change I could do IS to implement a sort function!)  
    sort exampleFile.txt

To remove duplicates though just calling sort isn't enough, instead I had to expand it and include this 
    | uniq -u 

But I didn't honestly want to have the files names be changed (I like the clairty!) so I had to make temporary files. I personally arbitrarily chose .bak files because they just seemed simple to use and kept the same name but changed .txt to .bak
    mv exampleFile.txt exampleFile.bak

Now I did this though I needed to have it so that after the sorting was finished I put it back to it's original name and extension (as in, to a .txt file). I did it using the Linux > operator and so I shoved all of the output into the file specified after the symbol.
    sort exampleFile.bak > exampleFile.txt

Putting this all together I came up with this lovely little line:
    mv exampleFile.txt exampleFile.bak && sort exampleFile.bak | uniq -u > exampleFile.txt

...Now of course one needs to realize that I have absolutely no ambition to rehash this every time I need to do this. So how did I solve this (lazy. lazy. lazy. lazy) problem? I made a shellscript... and this is infact in the repo as thisIsTheSortCommand file!
I achieved this by just adding the following at the top of my file
    #!bin/sh 

Then I used chmod 755 to make this into something that can run 
    chmod 755

Following this, anytime I wanted to use all of these sort functions on all of the files that we were given/specified to do so I would be able to call the following line from the terminal.
    ./thisIsTheSortCommand

#### The Actual Loading



###MISC.
#### Files:
#####"1k.txt" 
 DESCRIPTION: ... Slightly more than 1,000 reviews. Closer to 1,000,000 reviews but not exactly 1million. This is a huge text file and has been placed here exclusively for testing purposes.

* Why this insanely large file? Because I want to be confident that the programs we run can hold some volume of information, yet in the real world in practice even 1million entries is terrifyingly small. However for the scope of this project I don't see any need to try and process a 1billion (or more) line file. 

#####10.txt
DESCRIPTION: This file is actually just going to have 10 reviews placed within itself, nice and short. This is also the simplest example file and there are the expected outputs post-processing out on the wiki.
