#This is a simple python program to read and write files...i had many errors at first but this is the format i found to be working.
#If you know a more effective way of writting this script please tell me.Thanks in advance :) 
#Oh and you can also improve it.
from sys import argv,exit
import random

script,atom = argv

tup1 = ('okay','k','sure','yeah','yes')
tup2 = ('Hurray','Yay!!','Marvelous','Awesome','Right on bro')
tup3 = ('no','nope','nah','')
print "Hello am Atom, i can help you write files and store them."
print "Would you like to write some files?"
answ = raw_input(">")
for word in tup1:
	if answ == word:
		print random.choice(tup2)
		print "Lets get started then."

for word in tup3:
	if answ == word:
		print "Okay,maybe some other time.Bye"
		exit(0)


		
		

print "Let me first open the file to write in..."
target = open(atom,'w')
print "All done...now lets write some stuff."
print "Let\'s for now only have 3lines."

line1 = raw_input("Write line1 here:")
line2 = raw_input("Write line2 here:")
line3 = raw_input("Write line3 here:")

print "Now am going to write these to the file...it wont be long...promise."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print "Am done."


print "If you want we can open the file to view what you have written.\nDo you want to?"
decide = raw_input(">")

for word in tup1:
	if decide == word:
		print random.choice(tup2)
		print "let me open..."
		print "Here is your file."
		target = open(atom)
		print target.read()
		
for word in tup3:
	if answ == word:
		print "Okay,maybe some other time.Bye"
		exit(0)