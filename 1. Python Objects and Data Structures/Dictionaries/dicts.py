# Dictionaries have {key:value pairs}
# Dictionaries objects retrieved by key name.
# Dictionaries are unordered and cannot be sorted
dict1 = {"k1": "v1", "k2": "v2", "k3": "v3", "k4": "v4"}
print(dict1)
msrp = {"Mustang": 50000, "Corvette": "80000", "Charger": 30000}
print(msrp["Mustang"])
diff_data_types = {"key1": 22.22, "key2": ["can", "hold", "lists"], "key3": {"dict in dict key": "dict in dict value"}}
print(diff_data_types["key2"])
print(diff_data_types["key3"]["dict in dict key"])  # key 3-dictionary inside a dict, & gets value for the inside key
print(diff_data_types["key2"][2])  # prints the index 2 of the list in the dictionary loc at key 2
# get a k:v pair that's a list an item in the list uppercase
make_list = diff_data_types["key2"]
print(make_list)
make_upper = make_list[1]
print(make_upper)
print(make_upper.upper())
print(diff_data_types["key2"][2])
print(diff_data_types["key2"][2].upper())  # a quicker way to make item in list inside dict uppercase
diff_data_types["key4"] = "string"  # adds a key
print(diff_data_types)
print(diff_data_types.keys())  # displays keys
print(diff_data_types.values())  # displays values
print(len(diff_data_types))  # prints num of k:v pairs
print(diff_data_types.items())  # prints items in dict as tuples ()
