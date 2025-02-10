


#ADDING VALUES TO A DICTIONARY
character_dict["key"] = value # to add a key and value pair to the dictionary.

#ACCESSING VALUES FROM A DICTIONARY
print(character_dict["key"]) # prints "value"


#SETTING DICTIONARY VALUES
names = ["jack bronson", "jill mcarty", "john denver"]

names_dict = {}
for name in names:
    # .split() returns a list of strings
    # where each string is a single word from the original
    name_list = name.split()

    # here we update the dictionary
    names_dict[name_list[0]] = name_list[1]

print(names_dict)
# Prints: {'jack': 'bronson', 'jill': 'mcarty', 'john': 'denver'}

#USE in KEYWORD TO RETURN A BOOLEAN TRUE/FALSE - uiseful for counting.
if char in character_dict
    character_dict[key] += 1
else:
    character_dict[key] = 1