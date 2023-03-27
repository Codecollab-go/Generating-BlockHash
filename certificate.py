import hashlib
import datetime

name = "Rehan Sharmma"
date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# create a hash of the certificate data using SHA-256
certificate_data = f"{name}{date}".encode('utf-8')
certificate_hash = hashlib.sha256(certificate_data).hexdigest()

print("Certificate:")
print(f"Name: {name}")
print(f"Date: {date}")
print(f"Hash: {certificate_hash}")




# In this code, we define the certificate data as the name of the recipient and 
# the current date and time. We then concatenate the data into a single string and 
# encode it as bytes using the UTF-8 encoding.

# Next, we create a SHA-256 hash of the certificate data using the hashlib.sha256() 
# method, and we call the hexdigest() method on the hash object to generate a 
# hexadecimal string representation of the hash.

# Finally, we print the certificate data along with the hash value to the console.

# Note that in a real certificate, you would typically include additional fields, 
# such as the issuer's name, a serial number, and a public key. You would also sign 
# the certificate using a private key to ensure its authenticity.