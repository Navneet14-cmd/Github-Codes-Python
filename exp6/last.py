movies = {}
n = int(input("Enter the number of movies: "))
for i in range(n):
    name = input("Enter movie name: ")
    year = int(input("Enter release year: "))
    director = input("Enter director name: ")
    production_cost = float(input("Enter production cost: "))
    collection_made = float(input("Enter collection made: "))
    movies[name] = {
        "Year": year,
        "Director": director,
        "Production Cost": production_cost,
        "Collection Made": collection_made
    }
print("\na) All movie details:")
for name, details in movies.items():
    print(f"\nMovie Name: {name}")
    for key, value in details.items():
        print(f"{key}: {value}")
print("\nb) Movies released before 2015:")
for name, details in movies.items():
    if details["Year"] < 2015:
        print(name)
print("\nc) Movies that made a profit:")
for name, details in movies.items():
    if details["Collection Made"] > details["Production Cost"]:
        print(name)
director_name = input("\nEnter the director name to find their movies: ")
print(f"\nd) Movies directed by {director_name}:")
for name, details in movies.items():
    if details["Director"].lower() == director_name.lower():
        print(name)
