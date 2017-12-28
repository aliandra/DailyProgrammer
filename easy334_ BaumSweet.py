def baumSweet(n):
    """
    Returns the Baum-Sweet value of n
    """
    # Baum-Sweet value of 0 is 1 by definition
    if n == 0:
        return 1

    # binary representation of n
    binary = "{0:b}".format(n)

    # check for odd length blocks of consecutive 0's
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
    Returns the Baum-Sweet sequence from 0 to n in list form.
    The Baum-Sweet sequence in an infinite automatic sequence of 0's and 1's
    defined by:
        b_n = 1     if the binary representation of n contains no blocks of
                    consecutive 0's of odd length;
        b_n = 0     otherwise;
    """
    sequence = []
    for i in range(n + 1):
        sequence.append(baumSweet(i))
    return sequence


def test():
    print(baumSweetSequence(20))
    answer = [1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0]
    print(baumSweetSequence(20) == answer)


test()
