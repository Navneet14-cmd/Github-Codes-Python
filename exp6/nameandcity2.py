dict={}
list1=[]
list2=[]
str1=""
str2=""
n=int(input("Enter the number of person you want to enter: "))
for i in range (1,n+1,1):
    key=input("Enter the name of the student: ")
    value=input("Enter the city of the student: ")
    dict[key]=value
for key in dict.keys():
    list1.append(key)
for value in dict.values():
    list2.append(value)
for i in range (0,len(list1),1):
    str1=str1+" "+list1[i]
    str2=str2+ " "+list2[i]
print(str1)
print(str2)
count={}
for value in dict.values():
    if value in count:
        count[value]+=1
    else:
        count[value]=1
print(count)
        
 
    
