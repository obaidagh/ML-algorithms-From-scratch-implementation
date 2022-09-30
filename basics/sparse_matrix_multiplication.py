
def non_zero_dict(matrix):
    non_zero={}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]!=0:
                non_zero[(i,j)]=(matrix[i][j])
    return non_zero
                


def sparse_matrix_multiplication(matrix_a, matrix_b):

    b_Rows = len(matrix_b)

    a_Cols = len(matrix_a[0])
    a_Rows = len(matrix_a)
    b_Cols = len(matrix_b[0])

    if  a_Cols!= b_Rows:
        return [[]]

    else:
        matrix_c= [([0]*b_Cols) for i in range(a_Rows)]

        a_non_zero=non_zero_dict(matrix_a)
        b_non_zero=non_zero_dict(matrix_b)

        
        
            
        for i,k in a_non_zero.keys():
            for j in range(b_Cols): 
                if (k,j) in b_non_zero.keys():
                    matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j] 
        return matrix_c
