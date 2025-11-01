def min_max(nums):
    if not nums:
        raise ValueError("Список пуст")
    return (min(nums), max(nums))

def unique_sorted(nums):
    return sorted(set(nums))

def flatten(mat):
    result = []
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError("Элемент матрицы не список и не кортеж")
        for item in row:
            if isinstance(item, str):
                raise TypeError("Строка не является допустимым элементом матрицы")
            result.append(item)
    return result

print(min_max([3, -1, 5, 5, 0]))       
print(min_max([42]))                  
print(min_max([-5, -2, -9]))          
# print(min_max([]))                   
print(min_max([1.5, 2, 2.0, -3.1]))  

print(unique_sorted([3, 1, 2, 1, 3]))              
print(unique_sorted([]))                             
print(unique_sorted([-1, -1, 0, 2, 2]))             
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))          

print(flatten([[1, 2], [3, 4]]))                     
print(flatten([[1, 2], (3, 4, 5)]))                  
print(flatten([[1], [], [2, 3]]))                     
# flatten([[1, 2], "ab"])                            
