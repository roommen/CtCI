'''
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column is set to 0.
'''


def matrix_row_column_zero(mxn_matrix_):
    row = 0
    zero_row_column = list()
    for row_ in mxn_matrix_:
        column = 0
        for column_ in row_:
            if column_ == 0:
                zero_row_column.append([row, column])
            column += 1
        row += 1

    for zero_item in zero_row_column:
        mxn_zero_row = [0 for _ in mxn_matrix_[zero_item[0]]]
        mxn_matrix_.pop(zero_item[0])
        mxn_matrix_.insert(zero_item[0], mxn_zero_row)

        row = 0
        for _ in mxn_matrix_:
            mxn_matrix_[row][zero_item[1]] = 0
            row += 1

    return mxn_matrix_

if __name__ == '__main__':
    mxn_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 0, 12]]
    print(*matrix_row_column_zero(mxn_matrix))
