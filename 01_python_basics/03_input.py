# Input + Type Conversion:-

# # input()

# name=input("Enter Your Name:");
# print(name);

# age=int(input("Age:"))
# print(type(age));

# Multiple Assignment
# a,b=map(int,input("Enter Two Numbers:").split())
# print(a,b);

# Taking an Array as Input
# arr=list(map(int,input("Enter Numbers:").split()));
# print(arr);

# n=int(input("N: "));
# arr=list(map(int,input("Elements: ").split()));
# print(n);
# print(arr);

# Practice Questions — Input + Type Conversion

# Q1
# name=input("Enter Your Name: ");
# print("Hello",name);

# Q2
# num=int(input("Enter Number: "));
# print("Square is: ",num*num);

# Q3
# a,b=map(int,input("Enter Two Numbers: ").split());
# print("Addition: ",a+b);
# print("Subtraction: ",a-b);
# print("Multiplication: ",a*b);

# Q4
# arr=list(map(int,input("Enter Elememts: ").split()));
# print(arr);

# Q5
# arr=list(map(int,input("Enter Elements: ").split()));
# total=0;
# for i in range(len(arr)):
#     total=total+arr[i]
# print(total);

# Q6
# arr=list(map(int,input("Enter Elements: ").split()));
# print(len(arr));

# Q7
# arr=list(map(int,input("Elements: ").split()));
# print("First Element: ",arr[0]);
# print("Last Element: ",arr[-1]);

# Q8
# n = int(input("N: "))
# arr = list(map(int, input("Elements: ").split()))
# print("N =", n)
# print("Array =", arr)

# Q9
# n = int(input("N: "))
# arr = list(map(int, input("Elements: ").split()))

# if len(arr) == n:
#     print("Valid")
# else:
#     print("Not Valid")
