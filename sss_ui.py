## Shamir's Secret Sharing ##

import numpy as np
from numpy.polynomial import Polynomial
import random

def init():
    print(''' __   __   __  
( (` ( (` ( (` 
_)_) _)_) _)_) 
''')

    print("Shamir's Secret Sharing\n")
    print("---")
    print("Welcome to Shamir's Secret Sharing!\n")
    print("With a little typing here, and a little algebra there,")
    print("you and your friends can securely share a secret.\n")

def populate_random_list(min_val, secret):
    random_list = [secret]
    for i in range(min_val-1):
        random_list.append(random.randint(0, secret))
    return random_list

################################## Preparation ###

def preparation():
    
    print("-------")

    secret = 1234
    min_val = 3
    num_shares = 6
    shares_list = []

    while True:
        usr_input = input("Enter a secret to share in base10: ")
        if usr_input.isdigit():
            secret = int(usr_input)
            break
        else:
            print("Please enter a number.")

    while True:
        usr_input = input("\nEnter the total number of shares: ")
        if usr_input.isdigit():
            num_shares = int(usr_input)
            break
        else:
            print("Please enter a number.")

    while True:
        usr_input = input("\nEnter the minimum number of shares to reconstruct: ")
        if usr_input.isdigit() and int(usr_input) <= num_shares:
            min_val = int(usr_input)
            break
        else:
            print("Please enter a number less than or equal to the total number of shares.")

    print("---")

    poly = np.polynomial.Polynomial(populate_random_list(min_val, secret))
    print("\nThis is your random polynomial with the secret:")
    print(poly)

    for i in range(num_shares):
        shares_list.append((i+1, poly(i+1))) # skip 0 because it's the secret
    print("\nThis is the list of shares:")
    print(shares_list)

    print("\nIt is important you give each person the ordered pair, not just the x or y value.")
    print("\nRemember, you need %s shares to reconstruct the secret.\nBe careful how you distribute them" % min_val)
    print("If you don't have enough shares, you will not be able to reconstruct the secret.")

################################## Reconstruction ###

def reconstruction():
    
    print("-------")
    
    given_shares = []
    print("\nEnter the shares you have, starting with the x then y.\nSend a EOF Error when you are finished.\n")
    while True:
        try:
            given_shares.append((int(input("Enter a share number: ")), int(input("Enter the share's value: "))))
        except EOFError:
            break
        except ValueError:
            print("Please enter a number.")
        print("")

    while True:
        print("\n\n" + str(given_shares))
        usr_input = input("\nConfirm this is the list of shares you have? (Y/n): ")
        if usr_input.lower() == 'y' or usr_input == '':
            break
        elif usr_input == "n":
            print("Please start over.")
            exit()
        else:
            print("Please type a valid letter.\n")

    x = np.zeros(len(given_shares))
    for i in range(len(given_shares)):
        x[i] = given_shares[i][0]

    y = np.zeros(len(given_shares))
    for i in range(len(given_shares)):
        y[i] = given_shares[i][1]

    xp = 0
    yp = 0
    for xi, yi in zip(x, y):
        yp += yi * np.prod((xp - x[x != xi]) / (xi - x[x != xi]))

    print("\nYour secret is: %s" % yp)
    print("If this is incorrect, then double check your shares and required number of shares to reconstruct.")

def learning():
    import time

    print("-------")
    print("\nIn this program, you can split a base10 secret into shares, and then reconstruct the secret from those shares.")
    print("However, you need to have the required number of shares to reconstruct the secret.")
    print("\nThis allows you to share a secret with your friends, and then only reconstruct the secret if you have a consensus.")

    print("--")

    print("\nEach person gets a ordered pair like (1, 42) that, when entered into the program, will be converted to the secret.")
    print("\nSSS uses Lagrange Basis Polynomials to reconstruct the secret from the given points.")
    print("The secret will be when x = 0, so solving for x = 0 with the given points allows you to reconstruct the secret.")

    print("\n\nLearn more about Shamir's Secret Sharing at:")
    print("https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing")

################################## Main ###

init()
try:
    while True:
        usr_input = input("Would you like to create shares, reconstruct a secret, or learn about this program? (c/r/l): ")
        if usr_input.lower() == 'c':
            preparation()
            break
        if usr_input.lower() == 'r':
            reconstruction()
            break
        if usr_input.lower() == 'l':
            learning()
            break
        else:
            print("Please type a valid letter.")
except KeyboardInterrupt:
    print("\n\nExiting...")