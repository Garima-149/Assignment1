#program to take multiple lines from user and print them

# Create an empty list named 'lines'
lines = []

print("Enter a message:")
while True:
    
    l = input()
    if l:
       
        lines.append(l)
    else:
        # If the entered line is empty, break out of the loop
        break

# Iterate through each line in the 'lines' list
for l in lines:
    print(l) 
	