def maxmin(data):
    max=data[0]
    min=data[0]
    for i in range (0,len(data),1):
        if (data[i]>max):
            max=data[i]
        if (data[i]<min):
            min=data[i]
    return max,min
sequence=[12,5,29,32,44,13]
print(maxmin(sequence))
