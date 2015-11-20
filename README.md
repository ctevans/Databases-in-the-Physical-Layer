# Databases-in-the-Physical-Layer
The goal of this project is to teach the concept of working with data in the physical layer. This is done by building an information retrieval system, using the Berkeley DB library for operating on files and indices. Your job in this project is to write programs that keep data in files and maintain indices that provide basic searches over data. 

This project is divided into three phases.

### Phase #1: Parsing
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
