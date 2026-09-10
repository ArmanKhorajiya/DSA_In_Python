# FUNCTION:-
# A function is a block of code that performs a specific task.

# Syntax:
# def function_name(paramteres):
    # code

# ex:
# def add(a,b):
#     return a+b;
# print(add(1,2));
# print(add(3,4));

# PARAMETERS AND ARGUMENTS:

# def add(a,b):
#     print(a+b);
# add(10,20);

# Here: a,b -> parameters
      # 10,20 -> arguments

# DSA Example:

# def array_sum(arr):
#     total=0;
#     for n in arr:
#         total+=n;
#     return total;
# arr=[10,20,30,40];
# result=array_sum(arr);
# print(result);

# Function for Maximum:

# def find_max(arr):
#     maximum=arr[0];
#     for n in arr:
#         if n>maximum:
#             maximum=n;
#     return maximum;
# arr=[12,45,7,89,23];
# print(find_max(arr));

# Multiple Return Values:

# def calculate(a,b):
#     return a+b,a-b;
# addition, subtraction= calculate(10,5);
# print(addition);
# print(subtraction);

# DSA Pattern:

# def count_even(arr):
#     count=0;
#     for n in arr:
#         if n%2==0:
#             count+=1;
#     return count;
# arr=[10,15,22,7,8,13,40];
# print(count_even(arr));

# Q1
# def square(n):
#     return n*n;
# print(square(25));

# Q2
# def iseven(n):
#     if n%2==0:
#         return True;
#     else:
#         return False;
# print(iseven(3));

# Q3
# def array_sum(arr):
#     total=0;
#     for i in arr:
#         total+=i;
#     return total;
# arr=[1,2,3,4];
# print(array_sum(arr));

# Q4
# def find_max(arr):
#     maximum=arr[0];
#     for i in arr:
#         if i>maximum:
#             maximum=i;
#     return maximum;
# arr=[1,2,3,4,5];
# print(find_max(arr));

# Q5
# def count_even(arr):
#     count=0;
#     for i in arr:
#         if i%2==0:
#             count+=1;
#     return count;
# arr=[1,2,3,4,5,6];
# print(count_even(arr));

# Q6
# the print directly shows the output
# the return sends the output to the code that called the function


# RECURSION PREVIEW:
# def count_down(n):
#     if n==0:
#         return
#     print(n);
#     count_down(n-1);
# count_down(5);

# Q1
# def greet(name="User"):
#     print("Hello",name)
# greet("Arman")

# Q2
# def multiply(a,b):
#     return a*b;
# print(multiply(2,3));

# Q3
# def is_positive(n):
#     if n>0:
#         return True;
#     else:
#         return False;
# print(is_positive(3));

# Q4
# def find_min(arr):
#     minimum=arr[0];
#     for i in arr:
#         if i<minimum:
#             minimum=i;
#     return minimum;
# arr=[8,3,15,2,10];
# print(find_min(arr));

# Q5
# def count_target(arr,target):
#     count=0;
#     for i in arr:
#         if i==target:
#             count+=1;
#     return count;
# arr=[2,5,2,8,2];
# target=2
# print(count_target(arr,target));

# Q6
# it throws errors because the variable x is a local variable not a global so if it trys to access it outside the function then it gives error.

# Q7
# def count_down(n):
    # while n>0:
    # print(n);
    # n-=1;
# count_down(5);