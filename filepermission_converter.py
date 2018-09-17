#!/usr/bin/python3
#Author: Soji
#version: v1.0
''' 
This script is to convert the Linux symbolic file permission to octal permission 
and the expected input for this code is "rwxrwxrwx" or "r-xr-xr-x". This script is build to work on python3.
'''
class symbolicp:

    def __init__(self, read, write, execute):
        self.read = read
        self.write = write
        self.execute = execute

    def read_ugo(self):
        if self.read == "r":
            return 4
        elif self.read == "-":
            return int(0)
 
   def write_ugo(self):
        if self.write == "w":
            return 2
        elif self.write == "-":
            return int(0)

 
   def execute_ugo(self):
        if self.execute == "x":
           return 1
        elif self.execute == "-":
            return int(0)

file_permission = input("Enter the symbolic value:")
f_p = file_permission.split()
for list in f_p:
   USR = symbolicp(list[0], list[1], list[2])
   GRP = symbolicp(list[3], list[4], list[5])
   OTH = symbolicp(list[6], list[7], list[8])


USR1 = (USR.read_ugo() + USR.write_ugo() + USR.execute_ugo())
GRP1 = (GRP.read_ugo() + GRP.write_ugo() + GRP.execute_ugo())
OTH1 = (OTH.read_ugo() + OTH.write_ugo() + OTH.execute_ugo())

print("The octal value is:",USR1,GRP1,OTH1)
