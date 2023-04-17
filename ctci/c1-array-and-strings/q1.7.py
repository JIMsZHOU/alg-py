'''
    Given an image represented by an NxN matrix, 
    where each pixel in the image is represented by an integer, 
    write a method to rotate the image by 90 degrees. Can you do this in place?
'''

class Solution:
    '''
        Break down the question:
            Transpose the matrix: To transpose a matrix, we reflect it along its main diagonal. To do this in place, we can iterate over the elements of the matrix above the main diagonal (i.e., for i in range(n): for j in range(i, n):), and swap each element (i, j) with its corresponding element (j, i). This operation swaps the rows and columns of the matrix, effectively reflecting it along its main diagonal and rotating it by 90 degrees counter-clockwise.
            Reverse each row of the matrix: After transposing the matrix, we need to rotate it by another 90 degrees clockwise. To do this, we can reverse each row of the transposed matrix. This operation swaps the columns of the matrix, effectively rotating it by 90 degrees clockwise.

        For example, let's say we have the following matrix:
            1 2 3
            4 5 6
            7 8 9

        To transpose this matrix, we iterate over the elements above the main diagonal and swap them with their corresponding elements:
            1 4 7
            2 5 8
            3 6 9

        To rotate this matrix by 90 degrees clockwise, we reverse each row of the transposed matrix:
            7 4 1
            8 5 2
            9 6 3

        And that's it! We've successfully rotated the matrix by 90 degrees clockwise in place.
    '''
    def rotate_matrix(self, matrix: list) -> list:
        n = len(matrix)

        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row of the matrix
        for i in range(n):
            matrix[i] = matrix[i][::-1]

        return matrix
