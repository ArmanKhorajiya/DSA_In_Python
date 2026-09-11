# RECURSION = A Function calling to itself.

# ex:
# def count_down(n):
#     if n==0:
#         return;
#     print(n);
#     count_down(n-1);
# count_down(5);

# Factorial Program:
def factorial(n):
    if n==0:
        return 1;
    return n * factorial(n - 1)
print(factorial(5));