def corner_sum(n):
    """Return the sum of each of the four corners that are distance n
    from the center.

    Math!
    I found the polynomial equations describing the values at the corners
    as a function of their distance from the center.

    To do this I used the repeated deltas method (is that what it's called?)
    Consider the growth of the top left corner and the differences
    between them:

        Table of deltas:
        1   7   21
        6   14
        8
    There isn't yet much to see here. With this method the differences must all
    be zero. We don't have enough points to see if that happens.
    We can generate more points by following the pattern and
    extending the square.

        Table of deltas:
        1   7   21  43
        6   14  22
        8   8
        0

    Now we're onto something!

    This is actually taking a sort of derivative of the function in question.
    Also note that this method only works for polynomials.
    We can see that the third iteration of deltas yielded zero, meaning that
    the third derivative of the function is zero. We have a second degree
    polynomial, giving it the form f(x) = a*x^2+b*x+c

    For three unknowns we need three equations.
    Luckily we have plenty of data points.
    f(0) = 1 = a*0^2 + b*0 + c
        c=1
    f(1) = 6 = a*1^2 + b*1 + c
        a + b + 1=6
        a + b=5
    f(2) = 8 = a*2^2 + b*2 + c
        4a + 2b + 1 = 8
        4a + 2b = 7
    From here it is just simple substitution to solve for a and b.

    Repeat this process for the values in each corner and the final answer
    becomes trivially easy.
    """

    if n == 0:
        # the case of 0 distance, in which the functions overlap
        return 1
    elif n > 0:
        # no overlap here, use the sum of the four corners
        return 16 * n**2 + 4 * n + 4


def super_sum(n):
    """Return the sum of all corners that are distances [0,n] from the center.
    """
    return sum(corner_sum(i) for i in range(n + 1))


def main():
    # print(corner_sum(2))
    print(super_sum((1001 - 1) // 2))


if __name__ == '__main__':
    main()
