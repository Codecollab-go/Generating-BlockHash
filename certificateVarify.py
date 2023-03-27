import hashlib
import datetime

name = "John Doe"
date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

certificate_data = f"{name}{date}".encode('utf-8')
certificate_hash = hashlib.sha256(certificate_data).hexdigest()

# assume the stored hash value is retrieved from a database or file
stored_hash = 'ae174d4838f1c8e55a5c5d426cf0b8aaf1e00b70c4cb4fa19d3f8d97971a129b'

# verify the certificate by comparing the stored hash with the newly generated hash
if certificate_hash == stored_hash:
    print("Certificate is valid.")
else:
    print("Certificate is not valid.")






#     In this code, we assume that the hash value of the certificate data is 
#     stored separately (e.g., in a database or file), and we retrieve the stored 
#     hash value as the stored_hash variable.

# We then generate a new hash value of the certificate data using the same method we 
# used to create the original certificate, and store it as the certificate_hash 
# variable.

# Finally, we compare the stored hash value with the newly generated hash value 
# using an if statement, and print a message indicating whether the certificate 
# is valid or not based on the comparison result.
