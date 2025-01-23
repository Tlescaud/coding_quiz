def key_exists(dictionary, key):
    # Iterate through the keys in the dictionary
    for k in dictionary:
        if k == key:
            return True
    return False

# Example usage
input_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_check = 'b'
print(key_exists(input_dict, key_to_check))  # Output: True


'''In this program:

The key_exists function takes two arguments: dictionary and key.

It iterates through each key in the dictionary using a for loop.

If the key matches the key we're checking for, the function returns True.

If the loop completes without finding the key, the function returns False.'''