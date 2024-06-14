#program to removes all punctuations fromm string
str1="Welcome,,to goa!"
punc=''',!%&;'''
for ele in str1:
    if ele in punc:
        str1 = str1.replace(ele, " ")
 
# printing result
print("The string after punctuation filter : " + str1)