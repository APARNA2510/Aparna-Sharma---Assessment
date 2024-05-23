def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the string is equal to its reverse
    return cleaned_str == cleaned_str[::-1]

def main():
    # Prompt the user to enter a string
    user_input = input("Enter a string: ")
    # Check if the input string is a palindrome
    if is_palindrome(user_input):
        print(f"The string '{user_input}' is a palindrome.")
    else:
        print(f"The string '{user_input}' is not a palindrome.")

if __name__ == "__main__":
    main()
 