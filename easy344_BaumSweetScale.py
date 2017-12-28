def baumSweet(n):
    """
    Return the Baum-Sweet value of n.

    The Baum-Sweet sequence in an infinite automatic sequence of 0's and
    1's defined by:
        b_n = 1     if the binary representation of n contains no blocks
                    of consecutive 0's of odd length;
        b_n = 0     otherwise;
    """
    # Baum-Sweet value of 0 is 1 by definition
    if n == 0:
        return 1

    # Binary representation of n
    binary = "{0:b}".format(n)

    # Check for odd length blocks of consecutive 0's
    length = 0
    for char in binary:
        #
        if char == '1':
            if length % 2 != 0:
                return 0
            length = 0
        else:
            length += 1
    if length % 2 != 0:
        return 0
    return 1


def baumSweetSequence(n):
    """
    Return the Baum-Sweet sequence from 0 to n in list form.
    """
    sequence = []
    for i in range(n + 1):
        sequence.append(baumSweet(i))
    return sequence


def test():
    answer = [1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0]
    assert baumSweetSequence(20) == answer
    print('Test passed')


test()


'''Favorite Response:

def baum_sweet(n):
    count = 0
    while n:
        if n & 1:
            if count & 1:
                 return "0"
        else:
            count += 1
        n >>= 1
    return "1"

def bs_sequence(n):
    print(", ".join(map(baum_sweet, range(n+1))))
'''