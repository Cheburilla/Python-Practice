from functools import cmp_to_key


def largest_number(n: int, numbers: str):
    def my_sort(x, y):
        if x+y > y+x:
            return -1
        elif x+y == y+x:
            return 0
        else:
            return 1
    return ''.join(i for i in sorted([i for i in numbers.split(' ')], key=cmp_to_key(my_sort)))


print(largest_number(input(), input()))
