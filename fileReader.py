import sys

f = open ("Python_ características y concurrencia.pdf", "rb")
l = f.read(1024)

f2 = open(".\probe.pdf",'wb')

while (l):
    #print (l)
    f2.write(l)
    l = f.read(1024)
f.close()
f2.close()