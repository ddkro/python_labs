def transpose(mat):
    if not mat:
        return []
    row_len = len(mat[0])
    for row in mat:
        if len(row) != row_len:
            raise ValueError("Рваная матрица")
    return [[row[i] for row in mat] for i in range(row_len)]

def row_sums(mat):
    if not mat:
        return []
    row_len = len(mat[0])
    for row in mat:
        if len(row) != row_len:
            raise ValueError("Рваная матрица")
    return [sum(row) for row in mat]

def col_sums(mat):
    if not mat:
        return []
    row_len = len(mat[0])
    for row in mat:
        if len(row) != row_len:
            raise ValueError("Рваная матрица")
    return [sum(mat[row][col] for row in range(len(mat))) for col in range(row_len)]

print(transpose([[1, 2, 3]]))          
print(transpose([[1], [2], [3]]))      
print(transpose([[1, 2], [3, 4]]))      
print(transpose([]))                  

# print(transpose([[1, 2], [3]]))      

print(row_sums([[1, 2, 3], [4, 5, 6]]))   
print(row_sums([[-1, 1], [10, -10]]))      
print(row_sums([[0, 0], [0, 0]]))           

# print(row_sums([[1, 2], [3]]))            

print(col_sums([[1, 2, 3], [4, 5, 6]]))    
print(col_sums([[-1, 1], [10, -10]]))     
print(col_sums([[0, 0], [0, 0]]))           

# print(col_sums([[1, 2], [3]]))             
