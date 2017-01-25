if __name__ == '__main__':
    print(problem5())



def problem5():
    from collections import Counter    
    c = Counter()    
    for counter in [count_prime_factors(i) for i in range(2,21)]:
            c = merge_counters(c, counter)

    product = 1
    for key in set(c):
         product *= (key ** c[key])

    return product



def merge_counters(counter1, counter2):
    """Merges counter2 onto counter1"""
    for key in set(counter2):
        if counter2[key] > counter1[key]:
            counter1[key] = counter2[key]

    return counter1



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
