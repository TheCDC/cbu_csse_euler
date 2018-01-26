def list_prime_factors_long ( input_value ):
    """Returns a list of all prime factors of a number"""
    
    prime_factors = []


    # Check 2

    while input_value % 2 == 0 and input_value > 1:
        prime_factors.append(2)
        input_value /= 2


    # Check remaining values until exhausted

    value_to_check = 3

    while input_value > 1:
        if input_value % value_to_check == 0:
            prime_factors.append(value_to_check)
            input_value /= value_to_check
        else:
            value_to_check += 2

    return prime_factors



def list_prime_factors  ( input_value ):
    """Returns a list of all prime factors of a number without duplicates"""
    prime_factors_long = list_prime_factors_long(input_value)
    
    # Check empty list
    if len( prime_factors_long ) == 0:
        return []

    prime_factors = [ prime_factors_long[0] ]
    previous_value = prime_factors_long[0]
    
    for factor in prime_factors_long:
        if factor != previous_value:
            prime_factors.append(factor)
            previous_value = factor
    
    return prime_factors



def largest_prime_factor ( input_value ):
    """Returns the largest prime factor of a number"""
    
    prime_factors = list_prime_factors_long( input_value ) 

    return prime_factors[len(prime_factors) - 1]



def count_prime_factors ( input_value ):
    from collections import Counter
    # Check 2

    counter = Counter()

    while input_value % 2 == 0 and input_value > 1:
        counter[2] += 1
        input_value /= 2


    # Check remaining values until exhausted

    value_to_check = 3

    while input_value > 1:
        if input_value % value_to_check == 0:
            counter[value_to_check] += 1
            input_value /= value_to_check
        else:
            value_to_check += 2

    return counter
