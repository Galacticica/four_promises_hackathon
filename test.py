from werkzeug.security import generate_password_hash, check_password_hash

password = input("")
print(password)
hash = generate_password_hash(password)
print(type(hash))
print(hash)
check = check_password_hash(hash, password)
print(check)