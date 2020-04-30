# # Look at a number and extract the primes:
# # extract_primes(73)   -> [3, 7, 73]
# # extract_primes(1313) -> [3, 3, 13, 13, 131, 313]

def CheckIfPrime(maybe_prime_num):
    
    if maybe_prime_num > 1:

        for i in range(2, maybe_prime_num):

            if maybe_prime_num % i == 0:
                return
        else:
            return maybe_prime_num
    else:
        return

def extract_primes(num):
    num_arr = []
    size_of_num = len(str(num))
    game_over = False
    
    start_i = 0
    end_i = 1

    start = 0
    end = 1
    while game_over != True:

        maybe_prime_num = int(str(num)[start:end]) #int(str(num)[start:end])
        num_arr.append(CheckIfPrime(maybe_prime_num))
        
        start += 1
        end += 1

        if start == 1 and end == size_of_num + 1:
            game_over = True

        elif end == size_of_num+1:
            end_i += 1
            end = end_i

            start = start_i

    arr = []
    for val in num_arr:
        if val != None:
            arr.append(val)

    return arr


print(extract_primes(73))
print(extract_primes(1313))
print(extract_primes(101))