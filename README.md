# Databases-in-the-Physical-Layer
The goal of this project is to teach the concept of working with data in the physical layer. This is done by building an information retrieval system, using the Berkeley DB library for operating on files and indices. Your job in this project is to write programs that keep data in files and maintain indices that provide basic searches over data. 

This project is divided into three phases.

#### Phase #1: Parsing
Given a huge dump of reviews... let's parse it into something that we can later load into a database and actually make use of.
This is written in python version 3.x, to run it I typically just called it on the commandline. This python file however EXPECTS
to have the following present:
*Give it some sort of input file. (For now I have this hard coded, I may make it more flexible later.

This file will CREATE the following files:

reviews.txt
pterms.txt
rterms.txt
scores.txt


#### Phase #2: Loading into our database (But before that... the ever essential sorting!)



#### Files:
#####"1k" 
 DESCRIPTION: ... Slightly more than 1,000 reviews. Closer to 1,000,000 reviews but not exactly 1million. This is a huge text file and has been placed here exclusively for testing purposes.

* Why this insanely large file? Because I want to be confident that the programs we run can hold some volume of information, yet in the real world in practice even 1million entries is terrifyingly small. However for the scope of this project I don't see any need to try and process a 1billion (or more) line file. 

