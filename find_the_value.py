# Define the dictionary
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Get input from the user
key = int(input("Enter the key: "))

# Check if the key exists in the dictionary and return the value
if key in d:
    print(f"The value for the key {key} is {d[key]}")
else:
    print("Key not found in the dictionary.")
