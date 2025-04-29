import re
text='''The Jim Corbett National Park, nestled in the foothills of the Himalayas in Uttarakhand, India, is a renowned wildlife sanctuary and one of the oldest national parks in the country, established in 1936. It is named after the famed British-Indian hunter and conservationist, Jim Corbett.
Spanning over 1,300 square kilometers, the park boasts a diverse range of habitats, including dense sal forests, grassy meadows, rivers, and rugged hills. Known as a haven for wildlife enthusiasts and nature lovers, the park is especially famous for its population of Bengal tigers. 
Visitors can also encounter other iconic species such as leopards, elephants, deer, wild boars, and an array of bird species, making it a birdwatcher’s paradise. Jeep safaris and elephant rides provide thrilling ways to explore the park's rich biodiversity.
Apart from its wildlife, Corbett offers picturesque landscapes that captivate photographers and adventurers alike.
The Ramganga River adds to the scenic beauty while also supporting aquatic life. Jim Corbett National Park is not just a destination for adventure; it's also a symbol of India's commitment to wildlife conservation, as it played a pivotal role in the launch of Project Tiger.
Its natural splendor and ecological importance make it a must-visit destination'''
A=re.match("The",text) #1
print(f"{A}\n")

B=(len(re.findall("the",text))) #2
print(f"{B}\n")

match=re.finditer("and",text) #3
for i in match:
    print(i)
print("\n")

C=re.search("to",text) #4
print(f"{C}\n")

E=re.sub("River","lake",text) #5
print(f"{E}\n\n")

print(re.search("^The",text)) #6
print(re.search("^the",text))
print("\n")

print(re.search("destination$",text))#7
print(re.search("jaguar$",text))
print("\n")

print(re.search("[abcth]",text))#8
print(re.search("[z]",text))
print("\n")

print(re.search("d.",text))
print(re.search("V.",text))
print("\n")


