import bcrypt


gen = bcrypt.gensalt()
hash = bcrypt.hashpw(password=b"password", salt=gen)

w = bcrypt.checkpw(b"123",hash)

print(hash)