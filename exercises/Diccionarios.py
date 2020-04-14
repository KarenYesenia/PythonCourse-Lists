# Data strucute -> lists, Dicts

# A dictionary is a data structure where we can have many data kinds grouped (as a list)
# The main difference between a dict and list is that in a list we only have values,
# Examples: Martín, Arturo, etc. Or [1,2,3,4,5].
#In dict we have a key-value pair values for each attribute into the dictionary.
# It means that now we have values into the diccionary, but each one of this values HAVE
#a key or identifier, a name which each attribute is identified.
# Also, the data int a dict is unordered

user = {
    "first_name": "Karen",
    "last_name": "Rivera",
    "age": 23,
    "Birth_date": "1996-11-21"
}
# Propiertes
# -Dictionaries are defined using curly braces
# -Each attribute needs to have the following sintax key: value and needs to have comma in the end of the line
# -Key are always string, so need to be quoted
# -Values cab be of many kinds (int,string,boolean,none,float) even data structures (list, data) 

# Ger a key of a dict:
print(user["first_name"])

#What happens if the key doesn´t exist
#print(user["gender"]) # Throw an error

#How can we check if a ky exist into a dict?

#print("first_name" in user)

if "gender" in user:
    print(user("gender"))
else:
    print("Gender key doesn´t exit")

if "last_name" in user:
    print(user["last_name"])
else:
    print("last_name key doesn´t exit")

# Check if a key exist in the dict, and put default

print(user.get("conuntry", "Mexico"))

# Add nem keys to a dict
user["email"] = "yesrkaren@gmail.com"
print(user)
print("update")


# Update Existing keys in a dict
user["email"] = "yesr-karen@gmail.com"
print(user)

# DELETE KEYS IN A DICT
del (user["email"])
print(user)

profile = {
    "profile_phoho": "pickachu.jpg",
    "RFC": "KAJFOE",
    "HOBBIES": "X" 
}
#cONCATENAR OR JOIN DICTS
user.update(profile)
print(user)

# Loop keys and values of a  dict
for key, value in user.items():
    print("************************************")
    print("Key:", key)
    print("Value:", value)