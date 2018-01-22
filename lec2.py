# Dictionary or Hash

countries = ["Italy", "Germany", "Spain", "USA", "Switzerland"]
dishes = ["pizza", "sauerkraut", "paella", "Hamburger"]

# converting two arrays to dict
country_specialities = zip(countries, dishes)
country_specialities = dict(country_specialities)

print(country_specialities)


key_Hash = dict()

for i in range(10):
    key_Hash[i] = chr(65 + i)

print(key_Hash.items())
print(key_Hash.keys())
print(key_Hash.values())

print(key_Hash[0], end=" ")
print(key_Hash.get(1))

# delete the last item
key_Hash.popitem()

print(key_Hash.items())

