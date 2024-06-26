user = {
    "username": "tombombadil",
    "first_name": "Tom",
    "last_name": "Bombadil",
    "age": 100
}

print(user)
# fetch value using key
print(user['age'])

# Adding new key value pairs
user['home'] = 'Withywindle, Middle-Earth'

# Updating already exisiting key
user['age'] = 99
print(user)

# deleteing a key/value pair
del user['home']
print(user)

# list all keys in dict
print(list[user])
# fetch sorted list of all keys from dict
print(sorted(user))
# use type to check the type, what is the type of sorted list conating keys of dict
print(type(sorted(user))) # <class 'list'>

# Check if key exist in dict
print('username' in user)

# ---------------------------------- Getting & Setting Dictionary Items ----------------------
print('Getting & Setting Dictionary Items')
# Keys are currently only items in list here
keys = ['username', 'first_name','last_name','age']
default_value = ''

# Creating dict keys using dict and providing default values using fromkeys
user_new = dict.fromkeys(keys,default_value)
print(user_new) # {'username': '', 'first_name': '', 'last_name': '', 'age': ''}

# Updating with new values
user_new['username'] = 'tombombadil'
user_new['first_name'] = 'Tom'
user_new['last_name'] = 'Bombadil'
user_new['age'] = 100
print(user_new) # {'username': 'tombombadil', 'first_name': 'Tom', 'last_name': 'Bombadil', 'age': 100}

# Get home , if does not exist just print doesn't exist
print(user_new.get('home', "doesn't exist"))
# Add new home key value pair
user_new['home'] = 'Withywindle, Middle-Earth'
# Now get home , doesn't exist will not be shown now
print(user_new.get('home', "doesn't exist"))
print(user_new)

# delete home
del user_new['home']
print(user_new)

# Create list of all the keys
print(list(user_new.keys()))
# Create list of all the values
print(list(user_new.values()))

# *** Creating dict from two lists, Advance concept ****
f = ['a','b']
g = [1,3]
new = dict(map(lambda i,j : (i,j) , f,g))
print(new) # {'a': 1, 'b': 3}

# ---------------------- Dictionary Methods -------------------------
print('A few dict methods')
user_new_extra = {
    "username": "tombombadil",
    "first_name": "Tom",
    "last_name": "Bombadil",
    "age": 100
}

print(user_new_extra)
# Returns a list containing a tuple for each key:value pair
print(user_new_extra.items())
# Returns the value of the specified keyname. Used in the previous unit. Returns default None if the keyname doesn't exist unless you override this default with a optional value.
print(user_new_extra.get('age', 0))
# Updates the dictionary with the specified key:value pairs
user_new_extra.update({'home': 'Withywindle, Middle-Earth'})
print(user_new_extra)
# Removes the last inserted key:value pair
print(user_new_extra.popitem())
print(user_new_extra)
# remove specific key value from dict
print(user_new_extra.pop('username'))
print(user_new_extra)
# Removes all the elements from the dictionary
user_new_extra.clear()
print(user_new_extra)
