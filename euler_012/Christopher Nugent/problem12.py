from prime_factorization import count_prime_factors

def count_factors( n ):
    pf_count = count_prime_factors(n).values()
    multi = 1
    for i in [j + 1 for j in pf_count]:
        multi *= i
    return multi
        
    

def problem12():
    i = 1
    triangle = 0
    while(True):
        triangle += i
        i += 1
        if count_factors(triangle) >= 500:
            return triangle 
       
    return -1



if __name__ == '__main__':
    print(problem12())
