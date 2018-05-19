#This script is to copy the data from one file to another

import time
from sys import argv
from os.path import exists

script,frm1,to1 = argv

#print "copying from %s to %s" %(frm1, to1)
#into = open(frm1)
#print into

pinto = open(frm1).read()


print "now we will check the size of the file, & its: %d" %len(pinto)
time.sleep(3)
print "lets check if the output file exist? \nIt's there:%r" %exists(to1) 
time.sleep(1)
print "So the files are the to initiate the copy \nshall we proceed? \nif so hit Enter!"
time.sleep(1)
raw_input(">")

print "copying the data from %s to %s" %(frm1, to1)
to = open(to1,'w')
to.write(pinto)


print "completed. \nnow verifying......"
#t1 = open(to1)
#t2 = t1.read()
t2 = open(to1).read()

print "The file size seems to be %r" %len(t2)
time.sleep(2)
print "Done."

to.close()




