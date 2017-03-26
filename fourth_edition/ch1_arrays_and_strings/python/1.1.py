'''
Implement an algorithm to determine if a string has all unique characters. What if you
can not use additional data structures?
'''

# Scenario 1 - Using a data structure of dictionary


def check_unique_characters_with_ds(str_):
    global alphabets
    unique_chars = dict()
    for alphabet in str_:
        if alphabet not in unique_chars:
            unique_chars[alphabet] = 1
        else:
            val = unique_chars[alphabet]
            unique_chars[alphabet] = val + 1

    for v in unique_chars.values():
        if v > 1:
            return "Not Unique"
        else:
            return "Unique"


if __name__ == '__main__':
    string = input()
    print(check_unique_characters_with_ds(string))


# Scenario 2 - Without using any data structures


def check_unique_characters_without_ds(str_):
    sorted_str = list(sorted(str_))
    try:
        for i in range(len(sorted_str)):
            if sorted_str[i] == sorted_str[i+1]:
                return "Not Unique"
            i += 1
            if i == len(sorted_str)-1:
                return "Unique"
    except IndexError:
        pass


if __name__ == '__main__':
    string = input()
    print(check_unique_characters_without_ds(string))
