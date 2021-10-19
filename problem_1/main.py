def sum_of_multiples(input: int) -> int:
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.

    expects: the upper edge to which you need to find the amount(in our case it is 1000) of all the multiples of 3 or 5.
    modifies: nothing
    returns: the sum of all the multiples of 3 or 5 below 1000.
    """
    answer_list = sum([el for el in range(input) if (el % 3) == 0 or (el % 5) == 0])
    return answer_list


if __name__ == '__main__':
    print(sum_of_multiples(1000))

