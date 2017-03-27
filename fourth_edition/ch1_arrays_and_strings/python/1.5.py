'''
Write a method to replace all spaces in a string with ‘%20’.
'''


def replace_spaces(string_):
    index_ = 0
    for letter in string_:
        if letter == ' ':
            new_str = string_[:index_] + '%20' + string_[index_+1:]
            string_ = new_str
            index_ += 2
        index_ += 1

    return string_


if __name__ == '__main__':
    str_ = str(input())
    print(replace_spaces(str_))
