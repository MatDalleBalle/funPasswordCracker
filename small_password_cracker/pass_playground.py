import time
from itertools import product

password = input("Enter a password to crack: ")
start = time.time()
chars = "abcdefghijklmnopqrstuvwxyz"

cracked = None
for length in range(1, len(password) + 1):
    for candidate in product(chars, repeat=length):
        attempt = "".join(candidate)
        if attempt == password:
            cracked = attempt
            break
    if cracked is not None:
        break

end = time.time()
elapsed = end - start

if cracked is not None:
    print(f"Password cracked in {elapsed:.2f} seconds")
    print(f"Password is {cracked}")
else:
    print(f"Password not found in charset after {elapsed:.2f} seconds")