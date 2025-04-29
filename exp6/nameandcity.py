thisdict={}
list1=[]
list2=[]
str1=""
str2=""
n=int(input("Enter the number of person you want to add: "))
for i in range (1,n+1,1):
    key=input("Enter the name : ")
    value=input("Enter the city : ")
    thisdict[key]=value
for key in thisdict.keys():
    list1.append(key)
for value in thisdict.values():
    list2.append(value)
for i in range (0,len(list1),1):
    str1=str1+ ' ' +list1[i]
    str2=str2+ ' ' +list2[i]
print("All the names are: ",str1)
print("All the citya are: ",str2)
print("The name of students along with city name are : ",thisdict)
citycount={}
for value in thisdict.values():
    if value in citycount:
        citycount[value]+=1
    else:
        citycount[value]=1
print("The number of students in city are: ",citycount)
    