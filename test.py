import hashlib

password = "Inder"

has_sting = hashlib.sha256(password.encode('utf-8')).hexdigest()
print(has_sting)