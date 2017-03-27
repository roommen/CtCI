'''
Write a method to decide if two strings are anagrams or not.
'''
from collections import Counter


def check_anagrams(str1_, str2_):
    dict_str1 = Counter(str1_).items()
    dict_str2 = Counter(str2_).items()
    return "Anagram" if dict_str1 == dict_str2 else "Not Anagram"

if __name__ == '__main__':
    str1 = str(input())
    str2 = str(input())
    print(check_anagrams(str1, str2))
