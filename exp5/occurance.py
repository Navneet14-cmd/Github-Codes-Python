str=input("Enter the string: ")
ltr=['Aa','Bb','Cc','Dd','Ee','Ff','Gg','Hh','Ii','Jj','Kk','Ll','Mm','Nn','Oo','Pp','Qq','Rr','Ss','Tt','Uu','Vv','Ww','Xx','Yy','Zz']
ltrcount=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print("The count of each number are : \n")
for i in range (0,26):
    for j in str:
        if j in ltr[i]:
            ltrcount[i]+=1
for i in range (0,26):
    if (ltrcount[i]>0):
        print(' ',ltr[i][0], ':',ltrcount[i])
        
