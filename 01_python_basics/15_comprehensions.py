# Python List Comprehension

# Normal Loop:

# number=[]
# for i in range(5):
#     number.append(i);
# print(number)

# Same thing with comprehension:-

# number=[i for i in range(5)]
# print(number)


# Transform values:
# nums = [1, 2, 3, 4]
# Normal:
# squares = []
# for i in nums:
#     squares.append(i * i)
# print(squares)

# By Comprehension:
# squares = [num * num for num in nums]
# print(squares)


# With a Condition:
# Find Even Numbers

# Normal:
# even = []
# n = [1, 2, 3, 4, 5, 6]
# for i in n:
#     if i % 2 == 0:
#         even.append(i)
# print(even)

# Comprehension:
# even = [i for i in n if i % 2 == 0]
# print(even)

# Another ex:
# n = [1, 2, 3, 4, 5]
# double = [i * 2 for i in n]
# print(double)

# Practice
# Q1
# nums = [1, 2, 3, 4, 5]
# double = [i * 2 for i in nums]
# print(double)

# Q2
# nums = [1, 2, 3, 4, 5, 6]
# even = [i for i in nums if i % 2 == 0]
# print(even)

# Q3
# nums = [1, 2, 3, 4, 5]
# squares = [i * i for i in nums]
# print(squares)

# Q4
# nums = [1, 2, 3, 4, 5]
# squares = [i + 10 for i in nums]
# print(squares)

# Q5
# nums = [1, 2, 3, 4, 5, 6]
# odd = [i for i in nums if i % 2 == 1]
# print(odd)

# Q6
# nums = [1, 2, 3, 4, 5, 6]
# result = ["Even" if i % 2 == 0 else "Odd" for i in nums]
# print(result)

# Q7
# nums = [1, 2, 3, 4, 5]
# result = {i: i * i for i in nums}
# print(result)

# Q8
# nums = [1, 2, 3, 4, 5]
# result = {i: i * 10 for i in nums}
# print(result)

# Q9
# nums = [1, 2, 2, 3, 3, 4, 5]
# result = {i * i for i in nums}
# print(result)
