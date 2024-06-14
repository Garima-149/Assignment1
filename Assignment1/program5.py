#program to take string from user and writes it to a text file.
string=input("Enter any 6 length word:")
x=open("file1.txt","w")
x.write(string)
x.close()