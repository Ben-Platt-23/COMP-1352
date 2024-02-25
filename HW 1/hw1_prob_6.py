#6

def transpose_matrix(matrix):
    transposed_matrix = []
    
    for col in range(len(matrix[0])):
        transposed_row = []
        for row in range(len(matrix)):
            transposed_row.append(matrix[row][col])
        
        transposed_matrix.append(transposed_row)

    return transposed_matrix

original = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

result = transpose_matrix(original)

for row in result:
    print(row)