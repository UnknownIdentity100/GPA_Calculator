"""
import random
print("Hello, world!")
x = random.randint(1, 10)
def function1():
    for i in range(x):
        print(f"Printing a random number between 1 & 10: {x}")
function1()
"""

def Doorbell1():
    b_p = input("Was the doorbell pressed? (yes/no): ").strip().lower()
    if b_p == "yes":
        print("The doorbell was pressed.")
        k_p = input("Is the person known? (yes/no): ").strip().lower()
        if k_p == "yes":
            print("Hello there! Really good to see you! I'll be right with you!")
        else:
            print("Hello there! Please wait while I check who you are.")
    else:
        print("The doorbell was not pressed. No action taken.")
Doorbell1()

"""
import random
import time
import math
def random_number():
    return random.randint(1, 10)
def print_random_number():
    x = random_number()
    for i in range(x):
        print(f"Printing a random number between 1 & 10: {x + i + 1}")
    # This function generates a random number and prints it multiple times
        time.sleep(0.5)
          # Adding a delay to simulate processing time
print_random_number()
def calculate_square_root(number):
    if number < 0:
        return "Cannot calculate square root of a negative number."
    return math.sqrt(number)
def main():
    number = random.randint(1, 100)
    print(f"Calculating the square root of {number}...")
    result = calculate_square_root(number)
    print(f"The square root of {number} is: {result}")
if __name__ == "__main__":
    main()
    print_random_number()
    print("Program completed successfully.")
# This code generates a random number, prints it multiple times, and calculates the square root of another random number.
def calculate_cube():
    number = random.randint(1, 10)
    cube = number ** 3
    print(f"The cube of {number} is: {cube}")
calculate_cube()
def greet_user():
    name = input("Please enter your name: ")
    print(f"Hello, {name}! Welcome to the program.")
greet_user()
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def calculate_factorial():
    number = random.randint(1, 10)
    result = factorial(number)
    print(f"The factorial of {number} is: {result}")   
calculate_factorial()
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence
def print_fibonacci_sequence():
    n = random.randint(5, 15)
    fib_sequence = fibonacci(n)
    print(f"The first {n} numbers in the Fibonacci sequence are: {fib_sequence}")  
print_fibonacci_sequence()
def reverse_string(s):
    return s[::-1] 
def reverse_input_string():
    user_input = input("Please enter a string to reverse: ")
    reversed_string = reverse_string(user_input)
    print(f"The reversed string is: {reversed_string}")
reverse_input_string()
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
def check_prime_number():
    number = random.randint(1, 100)
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
check_prime_number()
def sum_of_list(lst):
    return sum(lst)
def calculate_sum_of_list():
    lst = [random.randint(1, 10) for _ in range(5)]
    total = sum_of_list(lst)
    print(f"The sum of the list {lst} is: {total}")
calculate_sum_of_list()
def find_max_in_list(lst):
    return max(lst)
def find_max_in_random_list():
    lst = [random.randint(1, 100) for _ in range(10)]
    max_value = find_max_in_list(lst)
    print(f"The maximum value in the list {lst} is: {max_value}")
find_max_in_random_list()
"""