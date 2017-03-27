'''
Design an algorithm and write code to remove the duplicate characters in a string
without using any additional bu#er. NOTE: One or two additional variables are !ne.
An extra copy of the array is not.
FOLLOW UP
Write the test cases for this method.
'''


# Assuming only lower case english alphabets and space
english_alphabets = "abcdefghijklmnopqrstuvwxyz "


def remove_dup_chars(string_):
    for letter in english_alphabets:
        letter_count = list(string_).count(letter)
        if letter_count > 1:
            for _ in range(letter_count - 1):
                string_.remove(letter)

    return string_


if __name__ == '__main__':
    str_ = input()
    print(*remove_dup_chars(list(str_)))


'''
***********
Test Cases:
***********
1. Check for all uppercase, lowercase and numbers
2. Check for spaces between words
3. Test for null character
4. Check for just spaces
'''
