#pogram that copies content from one text file to another
x=open('file1.txt','r')
copy=x.read()
x.close()

#another file
y=open('file2.txt','w')
y.write(copy)
y.close()