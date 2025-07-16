import numpy as np
#from python list or tuple(1d)
arr1=np.array([1,2,3,45,566,55])    
print("1d array:",arr1)
print(arr1.ndim)
print(arr1.size)
print(arr1.shape)
print(arr1.dtype)
print(arr1.itemsize)
#from list of list(2d)
arr2=np.array([[1,2,3,4],[10,12,14,16]])
print("2d array:",arr2)
print(arr2.ndim)
print(arr2.size)
print(arr2.shape)
print(arr2.dtype)
print(arr2.itemsize)
print("2.	Using built-in NumPy array creation functions:-----")
zeros_arr=np.zeros((2,4))#creates an array filled with zeroes np.zeros(shape)
print(zeros_arr)
ones_arr=np.ones((3,4))#creates an array filled with ones np.ones(shape)
print(ones_arr)
empty_arr=np.empty((1,3))#creates an array without initializing its entries np.empty(shape)
print(empty_arr)
arange_arr=np.arange(2,4,2)#creates an array with equaly spaced b/w elements with an interval np.arange(shape)
print(arange_arr)
linspace_arr=np.linspace(7,4,1)#creates an array with equaly spaced b/w elements over an interval np.linspace(shape)
print(linspace_arr)
full_arr=np.full((2,3),4)#creates an array of given shaped with filled values
print(full_arr)
identity_arr=np.identity(3)
print(identity_arr)#Creates an identity matrix (2D array with ones on the diagonal and zeros elsewhere).
print(np.dtype("int64"))
print("Arithmetic with NumPy Arrays:--------")
arr_a = np.array([1, 2, 3])
arr_b = np.array([4, 5, 6])

print("\nArray A:", arr_a)
print("Array B:", arr_b)

# Addition
print("A + B:", arr_a + arr_b)

# Subtraction
print("A - B:", arr_a - arr_b)

# Multiplication (element-wise, not matrix multiplication)
print("A * B:", arr_a * arr_b)

# Division
print("A / B:", arr_a / arr_b)

# Exponentiation
print("A ** 2:", arr_a ** 2)
#scalar operation
arr_c = np.array([[1, 2], [3, 4]])
print("\nArray C:\n", arr_c)

print("C + 10:\n", arr_c + 10)
print("C * 2:\n", arr_c * 2)
#broadcasting

arr_d = np.array([[1, 2, 3], [4, 5, 6]]) # shape (2, 3)
arr_e = np.array([10, 20, 30])         # shape (3,)

print("\nArray D:\n", arr_d)
print("Array E:", arr_e)

# arr_e is broadcast across the rows of arr_d
print("D + E:\n", arr_d + arr_e)
#basic indexing and slicing
arr = np.array([10, 20, 30, 40, 50])
print("\nArray:", arr)
print("Element at index 0:", arr[0])
print("Element at index -1:", arr[-1])
print("Element at index 4:", arr[4])


matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nMatrix:\n", matrix)
print("Element at (0, 1):", matrix[0, 1]) # Row 0, Column 1
print("Element at (2, 2):", matrix[2, 2]) # Row 2, Column 2
print("Boolean indexing:-----")
data = np.array([10, 20, 30, 40, 50])
print("\nData:", data)
filter_cond = data > 25
print("Filter condition (data > 25):", filter_cond)
print("Filtered data (data > 25):", data[filter_cond])
#fancy indexing
print("fancy indexing-----------")
arr_fancy = np.array([100, 200, 300, 400, 500])
indices = [0, 2, 4]
print("\nArray for fancy indexing:", arr_fancy)
print("Elements at specific indices [0, 2, 4]:", arr_fancy[indices])

matrix_fancy = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
rows = [0, 2]
cols = [1, 0]
# Select elements (matrix_fancy[0, 1], matrix_fancy[2, 0])
print("\nMatrix for fancy indexing:\n", matrix_fancy)
print("Elements at specific (row, col) pairs:", matrix_fancy[rows, cols])
