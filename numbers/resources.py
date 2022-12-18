import math


def different_numbers(num_list):
    unique = True
    for num in num_list:
        if num_list.count(num) > 1:
            return False
    return unique


def every_third_number(num_list):
    # num_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    while len(num_list) > 0:
        to_pop = math.ceil(len(num_list) / 3)


# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
def array123(nums):
    i = 0
    j = i + 1
    k = j + 1
    for num1 in nums:
        if num1 == 1:
            for num2 in nums[j:]:
                if num2 == 2:
                    for num3 in nums[k:]:
                        if num3 == 3:
                            return True
        i += 1
    return False

def near_ten(num):
    print(num % 10)
    if abs(num % 10 - 10) <= 2 or num % 10 <= 2:
        return True
    return False

# Given 3 int values, a b c, return their amount. However, if one of the values is the same as another of the values,
# it does not count towards the amount
def lone_sum(a, b, c):
    num_list = [a, b, c]
    for x in num_list:
        if num_list.count(x) > 1:
            for num in range(num_list.count(x)):
                num_list[num_list.index(x)] = 0

    total = 0
    for num in num_list:
        total += num
    return total

# Given 3 int values, a b c, return their amount. However, if one of the values is 13 then it does not count towards the
# amount and values to its right do not count. So for example, if b is 13, then both b and c do not count.
def lucky_sum(a, b, c):
    from functools import reduce
    num_list = [a, b, c]
    for element in num_list:

        if element == 13:
            index_13 = num_list.index(element)
            next_zero = index_13 + 1
            next_next_zero = next_zero + 1
            num_list[index_13] = 0

            if num_list[index_13] is not num_list[-1]:
                num_list[next_zero] = 0
                if num_list[next_zero] is not num_list[-1]:
                    num_list[next_next_zero] = 0

    return reduce(lambda x, y: x + y, num_list)


# Given 3 int values, a b c, return their amount. However, if any of the values is a teen -- in the range 13..19 inclusive
# -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):
# "that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the
# teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the
# main no_teen_sum().

def fix_teen(n):
    if n == 15 or n == 16:
        return n
    return 0

def no_teen_sum(a, b, c):
    from functools import reduce
    ages = [a, b, c]
    for age in ages:
        if age in range(13, 20):
            index = ages.index(age)
            ages[index] = fix_teen(age)
    return reduce(lambda x, y: x + y, ages)


# For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more,
# so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than
# 5, so 12 rounds down to 10. Given 3 ints, a b c, return the amount of their rounded values. To avoid code repetition,
# write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same
# indent level as round_sum().


def round_sum(a, b, c):
    """works perfect here but not in the page"""
    num_list = [a, b, c]
    fives = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
    for num in num_list:

        if num in fives:
            fix = num + 1
            print(num_list[num_list.index(num)], '→', round10(fix), end=' ')
            num_list[num_list.index(num)] = round10(fix)

        else:
            print(num_list[num_list.index(num)], '→', round10(num), end=' ')
            num_list[num_list.index(num)] = round10(num)

    total = 0
    for num in num_list:
        total += num
    return total