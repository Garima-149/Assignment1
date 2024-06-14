#program tha converts string into list of its charcters
string1="Enter a number"
list=[]
for char in string1:#looping
    if(char==' '):
        continue
    list.append(char)

print(list)    