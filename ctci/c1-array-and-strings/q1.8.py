'''
    write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0
'''

class Solution:
    '''
        break down the question:
            1. find the 0 element
            2. mark the row and column have 0 element
            3. set the row and column to 0
    '''

    def setZeros(self, matrix: list) -> list:
        rows = set()
        cols = set()

        # Step 1: Find the rows and columns that need to be set to 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Step 2: Set all elements in the rows to 0
        for i in rows:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

        # Step 3: Set all elements in the columns to 0
        for j in cols:
            for i in range(len(matrix)):
                matrix[i][j] = 0

        return matrix