from itertools import product
from string import ascii_letters, digits

for iter in product(ascii_letters + digits, repeat=6):
    print(iter)
