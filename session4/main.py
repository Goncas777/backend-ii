import multiprocessing


def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)


def compute_factorial(n):
    result = factorial(n)
    print(f"Factorial of {n} is {result}")


if __name__ == "__main__":
    numbers = [3, 4, 5, 6]
    processes = []

    for number in numbers:
        process = multiprocessing.Process(target=compute_factorial, args=(number,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
