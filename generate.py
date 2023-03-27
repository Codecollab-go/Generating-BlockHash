import hashlib

data = input("Enter data to be hashed: ").encode('utf-8')
block_hash = hashlib.sha256(data).hexdigest()
print("Block hash:", block_hash)



# In this code, the input() function is used to take input from the user. 
# The input is then encoded as bytes using the encode() method with the UTF-8 
# encoding.

# Next, the hashlib.sha256() method is used to create a SHA-256 hash object, and 
# the hexdigest() method is called on this object to generate a hexadecimal string 
# representation of the block hash.

# Finally, the block hash is printed to the console using the print() function.

# Note that in a real blockchain application, the input data for each block would 
# typically be more complex and include transaction data, timestamps, and other 
# metadata. Also, the block hash would be generated using a more sophisticated 
# hashing algorithm and include additional fields, such as the previous block hash 
# and a nonce value.