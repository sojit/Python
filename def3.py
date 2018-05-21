from sys import argv
import time

script, frm1 = argv

def pp_all(f):
    print f.read()

#def rewind(f):
#    f.seek(0)

def p_a_line(l_c,f):
    print l_c, f.readline()

c_f = open(frm1)

print "The the whole file:"
pp_all(c_f)

time.sleep(2)
print "now we will rewind"
#rewind(c_f)


print "let print three line"
time.sleep(3)

cu_lin = 1
p_a_line(cu_lin, c_f)

cu_lin = cu_lin+1
p_a_line(cu_lin, c_f)

cu_lin = cu_lin+1
p_a_line(cu_lin, c_f)
