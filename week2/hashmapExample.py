# Creating a hashmap
my_dict = {}

# Adding key-value pairs
my_dict['apple'] = 3
my_dict['banana'] = 5
my_dict['orange'] = 2

# Accessing values using keys
print("Number of apples:", my_dict['apple'])
print("Number of bananas:", my_dict['banana'])
print("Number of oranges:", my_dict['orange'])

# Modifying values
my_dict['banana'] += 2
print("Updated number of bananas:", my_dict['banana'])

# Checking if a key is in the hashmap
if 'grape' in my_dict:
    print("Number of grapes:", my_dict['grape'])
else:
    print("Grapes not found in the hashmap")

# Additional dictionary methods
print("\nAdditional Dictionary Methods:")

# clear() method: Removes all elements from the dictionary
my_dict.clear()
print("After clear():", my_dict)

# copy() method: Returns a shallow copy of the dictionary
original_dict = {'apple': 3, 'banana': 5, 'orange': 2}
copied_dict = original_dict.copy()
print("Copied Dictionary:", copied_dict)

# fromkeys() method: Creates a new dictionary with specified keys and a default value
keys = ['apple', 'banana', 'orange']
default_value = 0
new_dict = dict.fromkeys(keys, default_value)
print("New Dictionary from keys:", new_dict)

# get() method: Returns the value for the specified key, or a default value if the key is not found
print("Value for 'apple':", my_dict.get('apple', 'Key not found'))

# items() method: Returns a view of all key-value pairs in the dictionary
print("Items in the dictionary:", my_dict.items())

# keys() method: Returns a view of all keys in the dictionary
print("Keys in the dictionary:", my_dict.keys())

# values() method: Returns a view of all values in the dictionary
print("Values in the dictionary:", my_dict.values())

# pop() method: Removes and returns the value for the specified key
# Note: This will raise a KeyError if the key is not found (use get() for a safer option)
value_removed = original_dict.pop('banana')
print("Value removed for 'banana':", value_removed)
print("Updated Dictionary after pop:", original_dict)

# popitem() method: Removes and returns the last key-value pair in the dictionary
# Note: In Python 3.7 and later, this method removes and returns an arbitrary key-value pair
last_item_removed = original_dict.popitem()
print("Last item removed:", last_item_removed)
print("Updated Dictionary after popitem:", original_dict)

# setdefault() method: Returns the value for the specified key, or inserts a key with a default value if the key is not found
default_value = 0
value = original_dict.setdefault('grape', default_value)
print("Value for 'grape':", value)
print("Updated Dictionary after setdefault:", original_dict)

# update() method: Updates the dictionary with elements from another dictionary or from an iterable of key-value pairs
update_dict = {'peach': 4, 'pear': 6}
original_dict.update(update_dict)
print("Updated Dictionary after update:", original_dict)
