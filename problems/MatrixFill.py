'''
Created on: Mar 26, 2014

@author: qwang

Read from http://www.keithschwarz.com/interesting/code/?dir=matrix-fill. Python implementation
of this problem.

An algorithm that solves a creative Microsoft job interview question.

The question in this problem is the following: you are given a boolean
matrix of dimensions m x n. You want to transform the matrix to produce a
new matrix according to the following rule: entry (i, j) should be true
(we'll denote it '1') if there was a 1 anywhere on row i or column j, and
should be 0 otherwise. For example, given this input matrix:

                               0 0 0 1 0
                               1 0 0 0 0
                               0 0 0 0 0
                               0 0 0 1 0

the output would be

                               1 1 1 1 1
                               1 1 1 1 1
                               1 0 0 1 0
                               1 0 0 1 0

Similarly, given matrix

                                 0 0 0
                                 0 1 0
                                 0 0 0

The output would be

                                 0 1 0
                                 1 1 1
                                 0 1 0

The challenge is the following: is it possible to do this in time O(mn)
and space only O(1)? That is, can you solve this problem in constant space
and linear time? Amazingly, the answer is yes!

The initial problem with trying to solve this in O(1) space is that if we
start changing entries in the matrix from 0 to 1 as we begin filling in the
matrix, we might end up confusing ourselves later between the case where the
element was originally 1 (meaning we should fill its row and column with 1s)
and the case where the element was originally 0 (meaning that we shouldn't.)
I recommend trying to work through this problem before reading on - it's a
great challenge

* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

To motivate the correct solution, let's begin with a solution that uses
O(n) space rather than O(1) space.

If you think about it, for each row and each column, we only need to store
one bit of information: should that column be filled or not? Therefore, one
simple solution would be the following:

1. Create an array of size m storing which rows contain 1s. This can be
   filled in in time O(m) and uses O(m) space.
2. Create an array of size n storing which columns contain 1s. This can be
   filled in time O(n) and uses O(n) space.
3. For each (i, j), set position (i, j) to 1 if entry i in the row array or
   entry j in the column array is a 1. This also takes only O(mn) time.

This overall approach will use time O(mn), but needs space O(m + n), which
is too much for what we're trying to do.

However, we can reduce the space usage down to O(n) by using a clever
observation. Start as before by filling in an array that marks which
columns contain 1s. However, instead of creating a secondary array to store
this information for rows, instead just iterate across each row, filling it
with 1s if any of its entries are 1. After doing this, use the auxiliary
array with information about the marked columns to fill in the columns that
contain 1s. Why does this work? Well, if an element is a 0 in the result,
it means that there were no 1s in its row and no 1s in its column, so it
should indeed be a 0. If the element is a 1, then there was either a 1 in
its row or a 1 in its column, so it should indeed be a 1.

As an example, let's trace this algorithm on this input array:

                               0 0 0 1 0
                               1 0 0 0 0
                               0 0 0 0 0
                               0 0 0 1 0

We start off by making an auxiliary array for the columns and filling it in:

                               0 0 0 1 0
                               1 0 0 0 0
                               0 0 0 0 0
                               0 0 0 1 0

                               1 0 0 1 0 (aux array)

Next, we fill in each row containing a 1:

                               1 1 1 1 1
                               1 1 1 1 1
                               0 0 0 0 0
                               1 1 1 1 1

                               1 0 0 1 0 (aux array)

Finally, we fill each column with a 1 in the aux array:

                               1 1 1 1 1
                               1 1 1 1 1
                               1 0 0 1 0
                               1 1 1 1 1

                               1 0 0 1 0 (aux array)

and we're done!

This approach is more memory-efficient than before, but it's still using
too much memory. We need to get it down to O(1) memory, not O(n).

This is where we can use a really clever trick. Let's begin with an
observation: if every row in the matrix contains a 1, then the resulting
matrix will all be 1's. Therefore, we can start off our search by checking
if all the rows have a 1 in them and, if so, filling in the entire matrix.

If, however, some row is all zeros, we know that in the "fill in each row
that contains a 1" step, the row won't be touched. In fact, the only way
that any entries on this row will get set to 1 is if those entries are in
columns that contain 1s. But wait - that sounds a lot like our auxiliary
array, which should only have 1s in columns containing 1s! This leads us to
the most important insight of the algorithm: we can treat one of the rows of
zeros as our auxiliary array, meaning that we don't need to allocate a new
auxiliary array!

The new algorithm is pretty much the same as before, but with the auxiliary
array packed into the matrix itself. Let's do an example:

                               1 0 0 1 0 1
                               0 0 0 0 0 0
                               1 0 0 0 0 0
                               0 0 0 0 0 0
                               0 0 0 1 0 1

We start by scanning to find a row of all 0s to use as our auxiliary array.
This is shown here:

                               1 0 0 1 0 1
                               0 0 0 0 0 0 -- (aux)
                               1 0 0 0 0 0
                               0 0 0 0 0 0
                               0 0 0 1 0 1

Now, we fill in the auxiliary array, as before:

                               1 0 0 1 0 1
                               1 0 0 1 0 1 -- (aux)
                               1 0 0 0 0 0
                               0 0 0 0 0 0
                               0 0 0 1 0 1

Next, we fill in each row in the matrix containing at least one 1, *except*
for the auxiliary array row (after all, it's really all 0's. We're just
appropriating the bits for other purposes). This is shown here:

                               1 1 1 1 1 1
                               1 0 0 1 0 1 -- (aux)
                               1 1 1 1 1 1
                               0 0 0 0 0 0
                               1 1 1 1 1 1

Finally, using the auxiliary array, we fill in each column that contained a
1 in the initial array:

                               1 1 1 1 1 1
                               1 0 0 1 0 1 -- (aux)
                               1 1 1 1 1 1
                               1 0 0 1 0 1
                               1 1 1 1 1 1

And we're done! This whole process takes time O(mn) because we're making a
constant number of passes over the original matrix and only uses O(1) space
(enough to hold the index of the auxiliary array and incidental loop
variables).
'''

class MatrixFill(object):
    '''
    Implement matrix fill problem
    '''

    @classmethod
    def _find_aux_row(cls, matrix):
        # find out auxilary row, time O(mn)
        aux_row = -1
        row_index = 0
        for row in matrix:
            contain_1 = False
            for entry in row:
                if entry == 1:
                    contain_1 = True
                    break
            if not contain_1:
                aux_row = row_index
                break
            row_index += 1
        if aux_row == -1:
            # all rows contains 1, just fill matrix with 1 and return
            # time O(mn)
            for row in matrix:
                for i in range(len(row)):
                    row[i] = 1
        return aux_row, matrix

    @classmethod
    def _fill_aux(cls, aux_row, matrix):
        columns = len(matrix[0])
        for i in range(columns):
            contain_1 = False
            for j in range(len(matrix)):
                if j == aux_row:
                    continue
                if matrix[j][i] == 1:
                    contain_1 = True
                    break
            if contain_1:
                matrix[aux_row][i] = 1
        return matrix

    @classmethod
    def _fill_row(cls, aux_row, matrix):
        columns = len(matrix[0])
        index = 0
        for row in matrix:
            if index == aux_row:
                index += 1
                continue
            contain_1 = False
            for entry in row:
                if entry == 1:
                    contain_1 = True
                    break
            if contain_1:
                matrix[index] = [1] * columns
            index += 1
        return matrix

    @classmethod
    def _fill_column(cls, aux_row, matrix):
        rows = len(matrix)
        row = matrix[aux_row]
        j = 0
        for entry in row:
            if entry == 1:
                for i in range(rows):
                    matrix[i][j] = 1
            j += 1
        return matrix

    @classmethod
    def fill(cls, matrix):
        aux_row, matrix = cls._find_aux_row(matrix)
        if aux_row == -1:
            return matrix
        matrix = cls._fill_aux(aux_row, matrix)
        matrix = cls._fill_row(aux_row, matrix)
        matrix = cls._fill_column(aux_row, matrix)
        return matrix

if __name__ == '__main__':

    import sys

    def read_matrix(args):
        matrix = []
        for row in args:
            column = []
            for e in row:
                column.append(int(e))
            matrix.append(column)
        return matrix

    def print_matrix(matrix):
        for row in matrix:
            print ' '.join([str(e) for e in row])

    if len(sys.argv) < 2:
        print '''
        Usage: python MatrixFill.py 00001 10000 00100 11011
        '''
    matrix = read_matrix(sys.argv[1:])
    print 'Input Matrix: '
    print_matrix(matrix)
    result = MatrixFill.fill(matrix)
    print 'Output Matrix: '
    print_matrix(matrix)
