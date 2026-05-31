import threading
import time


def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)


def print_letters():
    for letter in ["A", "B", "C", "D", "E"]:
        print(letter)
        time.sleep(1)


def main():
    numbers_thread = threading.Thread(target=print_numbers)
    letters_thread = threading.Thread(target=print_letters)

    numbers_thread.start()
    letters_thread.start()

    numbers_thread.join()
    letters_thread.join()


if __name__ == "__main__":
    main()
