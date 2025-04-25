with open("city.txt", "w") as file:
    file.write("Dehradun 5.78 308.20\n")
    file.write("Delhi 190 1484\n")
    file.write("Mumbai 201 603.4\n")
    file.write("Chennai 71.5 426\n")
    file.write("Bangalore 84 709\n")
with open("city.txt", "r") as file:
    for line in file:
        cities=[line.split()]
data = []
for city in cities:
    city_name = city[0]
    population = float(city[1])
    area = float(city[2])
    data.append((city_name, population, area))
print("Details of all cities:")
for city in data:
    print(f"City: {city[0]}, Population: {city[1]} Lakhs, Area: {city[2]} sq KM")
print("\nCities with population more than 10 Lakhs:")
for city in data:
    if city[1] > 10:
        print(f"{city[0]}")
total_area = sum(city[2] for city in data)
print(f"\nTotal area of all cities: {total_area} sq KM")

