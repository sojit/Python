#import time
from sys import argv

script,filename = argv

#Pring the details about the script and the file which we goda read.
print "this is the filename", filename, "which we gona read & the script is %r" %script


#with the help of open(filename), I'm trying to read the content of the file.
txt=open(filename)

tet=open(filename,'w')
#Here I tried to print the content from the "txt"variable which I appended with the above command.
print txt.read()

#create a line of * to differencete the output simply
print "*"*90


#this will empty the file file name which we mentioned above i.e. tet
tet.truncate()


#here we are redirecting the stiring to the variables so that we can use it while write
line1 = "Onedatiwillgo"
line2 = "twoistwo"
line3 = "threeisthree"


#wrighting the variable values to the "tet" variable
tet.write(line1)
tet.write('\n')
tet.write(line2)
tet.write('\n')
tet.write(line3)
tet.write('\n')

#closing the tet variable which we used for writing.
tet.close()
