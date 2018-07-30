f = open('./test')
a = f.readlines()
print a
f.close()
a[2] = '3\n'
f = open('./test','w')
f.writelines(a)
f.close()

f = open('./test')
#for i in f.readlines():
    #print i
print f.read()
f.close()