def linear_search(lst, target):
    for item in lst:
        if item == target:
            return True
    return False


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9]
    print(linear_search(numbers, 5))
    print(factorial(5))
