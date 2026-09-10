# Lesson 6 - Loops in Python

# for Loop:
# Syntax:
# for variable in sequence:
    # code

# ex:
# for i in range(2,12,2):
#     print(i);

# range(start,stop,steps)

# Counting Backwards:
# for i in range(5,0,-1):
#     print(i);

# ex:
# arr=[10,20,30,40,];
# for num in arr:
#     print(num);

# Loop Using Index:
# arr=[10,20,30,40];
# for i in range(len(arr)):
#     print(i,arr[i]);


# while Loop
# A while loop repeats while a condition is true.
# i=1
# while i<=5:
#     print(i)
#     i+=1

# Find Sum in Array:
# arr=[10,20,30,40,50];
# total=0;
# for i in arr:
#     total=total+i;
# print(total);

# Find max:
# arr=[1,2,3,4];
# max=0;
# for i in arr:
#     if i>max:
#         max=i;
# print(max);

# Q5
# arr=list(map(int,input("Elements: ").split()));
# for i in range(len(arr)):
#     print(arr[i]);

# Q6
# arr=[5,10,15,20];
# sum=0;
# for i in arr:
#     sum+=i;
# print(sum);

# Q7
# arr=[12,45,7,89,23];
# maximum=arr[0];
# for i in arr:
#     if i>maximum:
#         maximum=i;
# print(maximum);

# Q8
# n=int(input("N: "));
# sum=0;
# for i in range(n+1):
#     sum+=i;
# print(sum);


# break and continue
# break:
# for i in range(1,10):
#     if i==5:
#         break;
#     print(i);

# continue
# for i in range(1,10):
#     if i==5:
#         continue;
#     print(i);

# DSA Example - Linear Search
# arr=[10,25,30,45,60];
# target=int(input("Enter Target to Find: "));
# for i in range(len(arr)):
#     if arr[i]==target:
#         print("Found at index: ",i);
#         break;

# Q1
# arr=[10,20,30,40,50];
# target=30;
# for i in arr:
#     if i==target:
#         print("Found");
#         break;

# Q2
# for i in range(1,21):
#     if i%3==0:
#         continue;
#     print(i);

# Q3
# arr=[5,12,7,20,9,30];
# for i in arr:
#     if i%2==0:
#         print(i);
#         break;

# Q4
# arr=[10,-5,20,-3,7,-8];
# for i in arr:
#     if i<0:
#         continue;
#     print(i);

# Q5
# 1,2,3


# NESTED LOOP:

# Basic Nested Loop
# for i in range(3):
#     for j in range(3):
#         print(i,j);

# Nested Loop with Numbers:
for i in range(1,4):
    for j in range(1,4):
        print(j,end=" ");
    print();

# Nested Loops for Patterns:
# for i in range(5):
#     for j in range(5):
#         print("*",end=" ");
#     print();

# Triangle Pattern
# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ");
#     print();

# NESTED LOOPS +ARRAYS
# arr=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         print(arr[i][j]," ",end=" ");
#     print();

# Q1
# for i in range(4):
#     for j in range(4):
#         print("*"," ",end=" ");
#     print();

# Q2
# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ");
#     print();

# Q3
# for i in range(1,6):
#     for j in range(i):
#         print(j+1," ",end=" ");
#     print();

# Q4
# arr=[
#     [10,20,30],
#     [40,50,60],
#     [70,80,90]
# ]
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         print(arr[i][j]," ",end=" ");
#     print();

# Q5
# 0 0
# 0 1
# 1 0
# 1 1
# 2 0
# 2 1

# Q1
# arr=[10,15,22,7,8,13,40];
# count=0
# for i in arr:
#     if i%2==0:
#         count+=1;
# print(count);

# Q2
# arr=[5,12,8,20,15,30];
# target=20;
# for i in range(len(arr)):
#     if arr[i]==target:
#         print("Found at index",i);
#         break;

# Q3
# arr=[2,5,2,8,2,10,5];
# target=2;
# count=0;
# for i in arr:
#     if i==target:
#         count+=1;
#         continue;
# print(count);