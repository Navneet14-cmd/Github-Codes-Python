string=input("Enter the string: ")
substring=input("Enter the substring: ")
count=0
length=len(substring)
for i in range (len(string)-length+1):
    if string[i:i+length] == substring:
        count+=1
print(count)
