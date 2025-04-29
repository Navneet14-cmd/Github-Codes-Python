import re
text = '''The Jim Corbett National Park, nestled in the foothills of the Himalayas in Uttarakhand, India, is a renowned wildlife sanctuary and one of the oldest national parks in the country, established in 1936. It is named after the famed British-Indian hunter and conservationist, Jim Corbett.
Spanning over 1,300 square kilometers, the park boasts a diverse range of habitats, including dense sal forests, grassy meadows, rivers, and rugged hills. Known as a haven for wildlife enthusiasts and nature lovers, the park is especially famous for its population of Bengal tigers.
Visitors can also encounter other iconic species such as leopards, elephants, deer, wild boars, and an array of bird species, making it a birdwatcher’s paradise. Jeep safaris and elephant rides provide thrilling ways to explore the park's rich biodiversity.
Apart from its wildlife, Corbett offers picturesque landscapes that captivate photographers and adventurers alike.
The Ramganga River adds to the scenic beauty while also supporting aquatic life. Jim Corbett National Park is not just a destination for adventure; it's also a symbol of India's commitment to wildlife conservation, as it played a pivotal role in the launch of Project Tiger.
Its natural splendor and ecological importance make it a must-visit destination'''


print("Testing '\\d' :")
matches = re.findall(r'\d', text)
print(matches)
print("\n FOR '\\D' :")
matches = re.findall(r'\D', text)
print(matches)
print("\n FOR '\\s' :")
matches = re.findall(r'\s', text)
print(matches)
print("\n FOR '\\S' :")
matches = re.findall(r'\S', text)
print(matches)
print("\n FOR '\\w' :")
matches = re.findall(r'\w', text)
print(matches)
print("\n FOR '\\W' :")
matches = re.findall(r'\W', text)
print(matches)
print("\n FOR '\\w+' :")
matches = re.findall(r'\w+', text)
print(matches)
print("\n FOR '\\b' :")
matches = re.findall(r'\bIndia', text)
print(matches)
print("\n FOR '\\B' :")
matches = re.findall(r'\BJeep\B', text)
print(matches)
print("\n FOR '\\A' :")
matches = re.findall(r'\AThe', text)
print(matches)
print("\n FOR '\\z' :")
matches = re.findall(r'destination\\z', text)
print(matches)