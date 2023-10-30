
#0(n!)
#This is the Heap´s algorithm, which is used for generating all possible permutation of n objects
#Another example could be the Travelling Salesman Problem
# <<def Permutation(data, n):
#     if n == 1:
#         print(data)
#         return
#     for i in range(n):
#         Permutation(data, n - 1)
#         if n % 2 == 0:
#             data[i], data[n-1] = data[n-1], data[í]
#         else:
#             data[0], data[n-1] = data[n-1], data[0]
# data = [1, 2]
# Permutation(data,len(data))>>


#O(2^n)
#Recursive calculation of Fibonacci numbers
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(30))
# def Permutation(data,n):
#     if n == 1:
#         print(data)
#         return
#     for i in range(n):
#         Permutation(data, n - 1)
#         if n % 2 == 0:
#             data[i], data[n-1] = data[n-1], data[i]
#         else:
#             data[0], data[n-1] = data[n-1], data[0]
# data = [1, 2]
# Permutation(data,len(data))

#O(n^)
# def Print_Pair(some_list):
#     for i in some_list: #n
#         for j in some_list: #n
#
#             print("Items: {}, {}".format(i,j))
# Print_Pair([1, 2, 3, 4])

# O(nlog(n))
# def Merge_Sort(data):
#     if len(data) <= 1:
#         return
#
#     mid = len(data) // 2
#     left_data = data[:mid]
#     right_data = data[mid:]
#
#     Merge_Sort(left_data)
#     Merge_Sort(right_data)
#
#     left_index = 0
#     right_index = 0
#     data_index = 0
#
#     while left_index <len(left_data) and right_index < len(right_data):
#         if left_data[left_index] < right_data[right_index]:
#             data[data_index] = left_data[left_index]
#             left_index += 1
#         else:
#             data[data_index] = right_data[right_index]
#             right_index += 1
#         data_index += 1
#
#     if left_index < len(left_data):
#         del data[data_index:]
#         data += left_data[left_index:]
#     elif right_index <len(right_data):
#         del data[data_index:]
#         data += right_data[right_index:]
#
# data = [9, 0, 8, 6, 2, 5, 7, 3, 4, 1]
# Merge_Sort(data)
# print(data)



