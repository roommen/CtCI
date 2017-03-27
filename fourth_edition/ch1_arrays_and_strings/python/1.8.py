'''
Assume you have a method isSubstring which checks if one word is a substring of
another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using
only one call to is_substring (i.e., “waterbottle” is a rotation of “erbottlewat”).
'''


def is_substring(s1, s2):
    if len(s1) != len(s2):
        return "Not a Rotation"
    if s2 in s1+s1:
        return "Rotation"
    else:
        return "Not a Rotation"


if __name__ == '__main__':
    s1 = str(input())
    s2 = str(input())
    print(is_substring(s1, s2))
