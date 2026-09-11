# RECURSION = A Function calling to itself.

# ex:
# def count_down(n):
#     if n==0:
#         return;
#     print(n);
#     count_down(n-1);
# count_down(5);

# Factorial Program:
# def factorial(n):
#     if n==0:
#         return 1;
#     return n * factorial(n - 1)
# print(factorial(5));

# Sum of 1 to n Numbers:
# def sum_n(n):
#     if n==0:
#         return 0;
#     return n+sum_n(n-1);
# print(sum_n(5));

# Q1
# def count_down(n):
#     if n==0:
#         return;
#     print(n);
#     count_down(n-1);
# count_down(5);

# Q2
# def factorial(n):
#     if n==0:
#         return 1;
#     return n*factorial(n-1);
# print(factorial(5));

# Q3
# def sum_n(n):
#     if n==0:
#         return 0;
#     return n+sum_n(n-1);
# print(sum_n(5));

# Q4
# def power(a,b):
#     if b==0:
#         return 1;
#     return a*power(a,b-1);
# print(power(2,4));

# Q5
# First
# test(4)
# 4==0 F
# return 4 + test(3)
# test(3)
# 3==0 F
# return 3 + test(2)
# test(2)
# 2==0 F
# return 2 + test(1)
# 1==0 F
# return 1 +test(0)
# test(0)
# 0==0 T
# Now, test(0)=1 and so on
# then answer is 10

# ex: factorial
# def factorial(n):
#     if n==0:
#         return 1;
#     return n * factorial(n-1);
# print(factorial(5));

# FIBONACCI SERIES(0 1 1 2 3 5 8 13 21.....):
# def fib(n):
#     if n==0:
#         return 0;
#     if n==1:
#         return 1;
#     return fib(n-1) + fib(n-2);
# # print(fib(40));

# Q1
# def fibo(n):
#     if n==0:
#         return 0;
#     if n==1:
#         return 1;
#     return fibo(n-1)+fibo(n-2);
# print(fibo(45));

# Q2
# fib(4) 4==0 F 4==1 F
# return fib(3)+fibp(2)
# fib(3) 3==0 F 3==1 F  fibo(2) 2==0 F 2==1 F
# return fib(2)+fib(1)  return fib(1)+fib(0)
# fib(2) 2==0 F 2==1 F  fib(1) 1==0 F 1==1 T    fib(1) 1==0 F 1==1 T    fib(0) 0==0 T return 0
# return fib(1)+fib(0)  return 1                return 1

# Q3
# def sum_digits(n):
#     if n==0:
#         return 0;
    
#     return(n%10)+sum_digits(n//10);
# print(sum_digits(1234));