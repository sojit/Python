import time
i = 0
numbers = []

while i<10: #while will run when the condition is True so it will run till i = 9, the while loop will close when the i =10.
   print "i is %d" %i #here we print value from the variable i
   numbers.append(i)  #append to the variable to the list

   i+=1 #increment the variable "i" +1
   time.sleep(1)
   print "numbers:%r" %numbers # print the values in the list 
   time.sleep(1)
   print "The value is after the increment %d" %i
   time.sleep(1)

for i in numbers: #calling the values from the list
    print "Here is the lists:%d" %i  #print the value from the list which is called in the variable i
