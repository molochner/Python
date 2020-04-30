# find the nth prime number
# how many prime numbers between 0 and num

def prime_number(num):

    maybe_prime = False
    prime = 0
    while prime <= num:
        test = 1
        j = 1
        while j > 0:
            #  check if prime
            if prime == num:
                return test - 1
            elif test == 2:
                prime += 1
                test += 1
                j = 1
            elif test % j != 0:
                maybe_prime = True
                j += 1
            elif test == j:
                if maybe_prime == True:
                    prime += 1
                    j = 1
                j = 1
                test += 1
            elif test / j == test:
                j += 1
            elif test % j == 0:
                maybe_prime = False
                j = 1
                test += 1

nth = int(input("Enter the nth prime number you want: "))

print(prime_number(nth))