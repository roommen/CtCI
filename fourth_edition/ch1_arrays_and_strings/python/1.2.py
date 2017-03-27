'''
Write code to reverse a C-Style String. (C-String means that “abcd” is represented as
!ve characters, including the null character.)
'''


def reverse_cstyle_string(string_):
    i = 2
    reverse_string = ""
    for _ in range(len(string_) - 1):
        reverse_string += string_[-i]
        i += 1

    return reverse_string


if __name__ == '__main__':
    str_ = input()
    # Make it C Style
    str_ += '\0'
    print(reverse_cstyle_string(str_))
