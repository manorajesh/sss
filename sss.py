## Shamir's Secret Sharing ##

import numpy as np
from numpy.polynomial import Polynomial
from scipy.interpolate import lagrange
import random

## Prepreparation ##

secret = 1234
min_val = 3
num_shares = 6
shares_list = []

def populate_random_list(min_val):
    global secret
    random_list = [secret]
    for i in range(min_val-1):
        random_list.append(random.randint(0, secret))
    return random_list

poly = np.polynomial.Polynomial(populate_random_list(min_val))

for i in range(num_shares):
    shares_list.append((i, poly(i+1)))
print(shares_list)

## Reconstruction ##

x = np.array([1,2,3])
y = 1234 + 166*x + 94*x**3
print(lagrange(x, y))