# Two variables can point to same list.
# a=[1,2,3];
# b=a;
# b.append(4);
# print(a);
# print(b);

# Creating a separate copy of a list.
# a=[1,2,3];
# b=a.copy();
# b.append(4);
# print(a);
# print(b);


# Mutable vs Immutable:-

# Mutable = can be changed.
# list  → mutable
# set   → mutable
# dict  → mutable

# Immutable = cannot be changed after creation.
# int    → immutable
# float  → immutable
# str    → immutable
# tuple  → immutable

# For example:
# name = "Arman"
# name[0] = "X"

# ❌ This gives an error because strings are immutable.

# But:

# arr = [10, 20, 30]
# arr[0] = 99

# ✅ This works because lists are mutable.


# DSA connection
# When you pass a list to a function
# def change(arr):
#     arr[0]=100;
# num=[1,2,3];
# change(num);
# print(num);

# Q1
# it prints [99,20]

# Q2
# [10,20]
# [99,20]

# Q3
# All but not string