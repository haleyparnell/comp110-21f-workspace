"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19_400
schools["Duke"] = 6_717
schools["NCSU"] = 26_150

# Print a dictionary literal representation
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students.")

# Remove a key-value pair from a dictionary
# by its key.
schools.pop("Duke")

# Test for the existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

# could also write this as...
if "Duke" in schools:
    print("Found the key 'Duke' in schools")
else:
    print("No key 'Duke' in schools")

# Update / Reassign a key-value pair
schools["UNC"] = 20_000
schools["NCSU"] += 200

print(schools)

# Demonstration of dictionary literals

# Example of empty dictionary literal
schools = {}  # Same as dict()
print(schools)

# Alternatively, initialize key-value pairs
schools = {"UNC": 19_400, "Dukie": 6_717, "NCSU": 26_150}
print(schools)

# What happens when a key does not exist?
print(schools["UNCC"])