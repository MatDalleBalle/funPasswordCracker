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

print()
print("─" * 40)
if cracked is not None:
    print("  ✓ Password cracked!")
    print()
    print(f"  Password:  {cracked}")
    print(f"  Time:      {elapsed:.2f} seconds")
else:
    print("  ✗ Password not found in charset")
    print()
    print(f"  Time:      {elapsed:.2f} seconds")
print("─" * 40)