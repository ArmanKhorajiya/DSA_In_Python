# What is an Array:
# An array stores multiple elements in an ordered sequence.
# arr=[10,20,30,40,50];
# Indexes:
# Value:   10   20   30   40   50
# Index:    0    1    2    3    4

# Access:
# print(arr[0])  # 10
# print(arr[3])  # 40

# Traversing an Array:
# Traversal means visiting every element.
# Using values:
# arr=[10,20,30,40];
# for i in arr:
#     print(i);

# Using indexes:
# arr=[10,20,30,40];
# for i in range(len(arr)):
#     print(arr[i]);

# Updating an Element:
# arr=[10,20,30,40];
# arr[0]=1;
# print(arr);

# Finding Sum:
# arr=[10,20,30,40];
# total=0
# for i in arr:
#     total+=i;
# print(total)

# Find Maximum:
# arr=[10,20,30,40];
# maximum=arr[0];
# for i in arr:
#     if i>maximum:
#         maximum=i;
# print(maximum);

# Q1
# arr=[10,20,30,40];
# minimum=arr[0];
# for i in arr:
#     if i<minimum:
#         minimum=i;
# print(minimum);

# Q2
# arr=[12,5,8,7,10,3];
# count=0;
# for i in arr:
#     if i%2==0:
#         count+=1;
# print(count);

# Q3
# arr=[10,15,20,25,30];
# print(25 in arr);

# Q4
# arr=[-5,10,-2,20,-8,15];
# total=0;
# for i in arr:
#     if i>0:
#         total+=i;
# print(total);