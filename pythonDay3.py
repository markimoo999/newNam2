a = raw_input("first name here\n")
b = raw_input("middle name here\n")
c = raw_input("last name here\n")
abc = a + " " + b + " " + c
length = len(abc)
lastLocation = abc.index(c)
countingE = abc.count("e")
countingA = abc.count("a")
print "your full name is " + abc +", and the length of your name is", length,"letters long, and the letter in the middle is "+ abc[length/2]+ ", and your last name is placed here in the code: " + str(lastLocation) + ", and your name has this many e's: " + str(countingE) + ", and this many a's: " + str(countingA) + "."
for x in range(0 , length):
    print abc[x] + "\n"
