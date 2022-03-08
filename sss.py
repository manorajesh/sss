## Shamir's Secret Sharing ##

import numpy as np
from numpy.polynomial import Polynomial
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
print(poly)

for i in range(num_shares):
    shares_list.append((i+1, poly(i+1))) #skip 0 because it's the secret
print(shares_list)

## Reconstruction ##

given_shares = [(1, 2563.0), (2, 6136.0), (3, 11953.0)]

x = np.zeros(len(given_shares))
for i in range(len(given_shares)):
    x[i] = given_shares[i][0]
print(x)

y = np.zeros(len(given_shares))
for i in range(len(given_shares)):
    y[i] = given_shares[i][1]
print(y)

xp = 0
yp = 0
for xi, yi in zip(x, y):
    yp += yi * np.prod((xp - x[x != xi]) / (xi - x[x != xi]))

print(yp)