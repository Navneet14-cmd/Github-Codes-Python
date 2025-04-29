sentence=input("Enter a sentence: ")
word=""
for i in sentence:
    if (i!=" "):
        word=word+i
    else:
        print(word)
        word=""
print(word)
