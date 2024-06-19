# Using readlines()
file1 = open('words.txt', 'r')
Lines = file1.readlines()
 
x = "Andrew123"

found = False

for line in Lines:
    if line in x:
        found = True

print(found)
print("Your ppassword contains a common word")

# replace x with the text input


