from utils import isPrime
def iscomposite(n):
    return not isPrime(n)

def test(n):
    """return true if number fits the conjecture"""
    # sum of a prime and twice a square
    # increase the square until n minus twice the square is never prime
    # n = p + 2*a**2, where p is prime 
    # p = n - 2*a**2
    # a = ((n-p)/2)**(1/2)

    for a in range(int((n/2)**(1/2)),0,-1):
        # print(n-2*i**2)
        # print(n,n-2*a**2,a)
        p = n-2*a**2
        if isPrime(p):
            return True
    return False
def main():
    tests = [9,15,21,25,27,33]
    assert all([test(i) for i in tests])
    # for i in [9,15,21,25,27,33]:
    #   print(i,test(i))
    n = 3
    # skip over primes
    while test(n) or isPrime(n):
        n+= 2
        if n%1000000 == 0:
            print("at",n)
    print(n)

if __name__ == '__main__':
    main()