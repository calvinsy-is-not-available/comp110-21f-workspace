"""We're demonstrating the abilities of dictionaries."""


# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# set a key-value pairing in the dictionary
schools["UNC"] = 19_400
schools["Duke"] = 6_717
schools["NCSU"] = 26_150

# print a dictionary literary expression
print(schools)

# access a value by its key (a look-up)
print(f" UNC has {schools['UNC']} students")

# remove a key-value pair from a dictionary
schools.pop("Duke")

# test for existence of a key
# is_duke_present: bool = "Duke" in schools
# print(f"Duke is present: {is_duke_present}")
if "Duke" in schools:
    print("Found the key 'Duke' in schools")
else:
    print("No key 'Duke' found in schools")

print(schools)

# update / reassign a key-vale pair
schools["UNC"] = 20_000
schools["NCSU"] += 200

# Demonstration of dictionary literals

# empty dictionary literal
schools = {}
print(schools)

# Alternatively, initialize key-value pairs
schools = {
    "UNC": 19400,
    "Duke": 6717,
    "NCSU": 26150
}

print(schools)
print(schools["UNCC"])
