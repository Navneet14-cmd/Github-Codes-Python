with open ("name.txt","w") as file:
    names=["Navneet","Anurag","kunal","tarun","Diwakar","Harshwardhan "]
    for name in names:
        file.write(name+"\n")
with open ("name.txt","r") as file:
    lines=file.readlines()
    total_names=len(lines)
vowel=0
for name in lines:
    if name[0].lower() in "aeiou":
        vowel+=1
longest=max(lines,key=len).strip()
print("Number of names are : ",total_names)
print("No of names starting with vowel :  ",vowel)
print("The longest name is : ",longest)
        
        