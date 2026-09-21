# Multiple Assignment:
# You can assign multiple values at once
# a,b=10,20;
# Very Useful For Swapping:
# a,b=b,a;

# in and not in:
# arr=[10,20,30];
# print(10 in arr);
# print(40 not in arr);

# range() with a step:
# for i in range(1,10,2):
#     print(i);
# Useful for jumping through indexes:
# Reverse
# for i in range(10,0,-1):
#     print(i);

# Unpacking:
# a,b,c=[10,20,30];
# print(a);
# print(b);
# print(c);

# any() and all():
# any() -> atleast one condition is true.
# arr=[1,2,3,4,4];
# print(any(x % 2!=0 for x in arr));

# all() -> every condition(means all elements should be passed with condtin) must be true
# arr=[2,4,6];
# print(all(x%2==0 for x in arr))

# while with two variables
# Common in two-pointer problems later:
# left=0;
# right=4;
# while left<right:
#     print(left,right);
#     left+=1;
#     right-=1;

# Q1
# a=10;
# b=20;
# a,b=b,a;
# print(a,b);

# Q2
# for i in range(2,11,2):
#     print(i);

# Q3
# 10

# Q4
# any() -> any elements should pass from given condition.

# Q5
# all() -> all elements should pass from given condition.


# Python List Comprehension

# Normal Loop:
# number=[]
# for i in range(5):
#     number.append(i);
# print(number)

# Same thing with comprehension
# number=[i for i in range(5)]
# print(number)

