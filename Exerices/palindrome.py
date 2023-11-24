def is_palindrome(input_string, start, end):
    # Base case: If the start index exceeds the end index, it means we've reached the middle of the string.
    if start >= end:
        return True

    # Recursive case: Check if the characters at the start and end indices match.
    if input_string[start] != input_string[end]:
        return False

    # If the characters match, recursively check the next pair of characters from the start and end.
    return is_palindrome(input_string, start + 1, end - 1)


def check_palindrome():
    input_string = input("Enter a string: ")
    start = 0
    end = len(input_string) - 1

    if is_palindrome(input_string, start, end):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

check_palindrome()