def fizz_buzz(start, end):
    if start < 1 or end > 100 or start > end:
        raise ValueError("Invalid range for FizzBuzz")

    for number in range(start, end + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

def main():
    try:
        fizz_buzz(1, 100)
    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    main()