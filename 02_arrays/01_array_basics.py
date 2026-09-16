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


# Linear Search:
# Linear search means checking elements one by one until we find the target.
# arr=[10,25,5,40,15];
# target=40;
# found=False
# for i in range(len(arr)):
#     if arr[i]==target:
#         print("Found at index",i);
#         found=True;
#         break;

# if not found:
#     print("Not Found");

# Search and Count:
# Sometimes we need to find how many times a target appears.
# arr=[2,5,2,8,2,5];
# count=0;
# target=2;
# for i in range(len(arr)):
#     if arr[i]==target:
#         count+=1
#         print("Found at Index:",i)
#         continue
# print(count);

# Q1
# arr=[10,20,30,40,50];
# target=30;
# for i in range(len(arr)):
#     if arr[i]==target:
#         print(i)
#         break;

# Q2
# arr=[10,20,30,40,50];
# target=100;
# Found=False;
# for i in arr:
#     if i==target:
#         Found=True
#         print("Found");
# if Found==False:
#     print("Not Found");

# Q3
# arr=[5,2,5,8,5,5,10];
# count=0;
# target=5;
# for i in arr:
#     if i==target:
#         count+=1;
# print(count);

# Q4
# arr=[3,7,2,7,9,7];
# target=7;
# for i in range(len(arr)):
#     if arr[i]==target:
#         print("Found at index:",i)
#         break;


# Insertion and Deletion:
# Insertion
# arr=[10,20,30,40,50];
# arr.insert(2,25);
# print(arr);

# Deletion
# arr=[10,20,30,40];
# arr.pop(1);
# print(arr);

# Q1
# arr=[10,20,30,40];
# arr.insert(2,25);
# print(arr);

# Q2
# arr=[10,20,30,40];
# arr.pop(1);
# print(arr);

# Q3
# arr=[10,20,30];
# arr.insert(0,5);
# print(arr);

# Q4
# arr=[10,20,30,20,40];
# target=20;
# for i in range(len(arr)):
#     if arr[i]==target:
#         arr.pop(i)
#         break;
# print(arr);


# Array Traversal Patterns
# Find an element satisfyiing a condition:
# Find the first even number
# arr=[7,9,11,8,15,20];
# for i in arr:
#     if i%2==0:
#         print("Found:",i)
#         break;

# Find the first positive number
# arr=[-5,-2,0,7,10];
# for i in arr:
#     if i>0:
#         print("Found:",i)
#         break;

# Q1
# arr=[2,4,8,10,7,9];
# for i in arr:
#     if i%2==1:
#         print("Found:",i)
#         break;

# Q2
# arr=[5,8,3,-4,-10];
# for i in arr:
#     if i<0:
#         print("Found:",i)
#         break;

# Q3
# arr=[5,2,7,5,9,5];
# target=5;
# for i in range(len(arr)-1,-1,-1):
#     if arr[i]==target:
#         print("Found at:",i);

# Q4
# arr=[10,5,20,8,20,15];
# largest=float("-inf");
# second=float('-inf');
# for i in arr:
#     if i>largest:
#         second=largest
#         largest=i;
#     elif i>second and i!=largest:
#         second=i;
# print(second);

