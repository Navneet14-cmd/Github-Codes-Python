a=input("Enter the string: ")
n=len(a)
counter=0
for i in range (0,n,1):
    if (a[i]== 'A' or a[i]=='E' or a[i]=='I' or a[i]=='O' or a[i]=='U' or a[i]== 'a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u') :
        counter+=1 
print("The numebr of vowels present in the string are : ",counter)        
        
