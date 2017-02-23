import prime_factorization as pf

def pe47( consecutive, factors ):
    itr = 1
    count = 0
    base = 0
    while(True):
        if len(pf.count_prime_factors(itr)) == factors:
            if count == 0:
                base = itr            
            count += 1
            if count == consecutive:
                return base
        else:
            count = 0
        itr += 1
        if itr % 10000 == 0:
            print(itr)


if __name__ == "__main__":
    print(pe47(4, 4))
