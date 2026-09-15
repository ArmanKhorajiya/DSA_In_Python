# TUPLE:-

# data=(10,20,30);
# print(data[0]);

# List vs Tuple:
# arr=[10,20,30]; #list
# data=(10,20,30); #tuple

# in list:
# arr[0]=100;
# # ✅ Allowed

# # in tuple:
# data[0]=100;
# # ❌ Error


# SET:-
# A set stores unique values.
# Duplicates are automatically removed.

# numbers={1,2,3,2,1};
# print(numbers);

# Add:
# numbers.add(4)

# Remove:
# numbers.remove(2);

# In Check Existence:
# print(3 in numbers);


# DICTIONARY:-
# It stores key -> value pairs.

# student={
#     "name":"Arman",
#     "age":18,
#     "marks":85,
# }
# # print(student["name"]);
# # print(student["marks"]);

# # # Add/Update:
# # student["city"]="Wankaner";

# # # Update:
# # student["marks"]=90;

# # # In Check key:
# # if "name" in student:
# #     print("Found");

# # Dictionary Traversal:
# # Keys:
# for key in student:
#     print(key);

# # Values:
# for value in student.values():
#     print(value);

# # Both:
# for key,value in student.items():
#     print(key,":",value);

# Dictionaries are very Important in DSA:
# Suppose:
# arr = [2, 5, 2, 8, 2, 5]

# We want to count each number.
# Using a dictionary:

# frequency = {}
# for num in arr:
#     if num in frequency:
#         frequency[num] += 1
#     else:
#         frequency[num] = 1
# print(frequency);

# Q1
# point=(10,20,30);
# print(point[1]);

# Q2
# nums=[1,2,2,3,3,4,4,5];
# a=set(nums);
# print(a);

# Q3
# nums={1,3,5,7,9};
# print(7 in nums);

# Q4
# student={
#     "name":"Arman",
#     "age":18,
#     "marks":85
# }
# print(student["marks"]);
# I understand this but how do we print specific students marks if there are more than one.

# Q5
# Find the frequency of every number:
# arr=[1,2,1,3,2,1,4];
# frequency={};
# for i in arr:
#     if i in frequency:
#         frequency[i]+=1;
#     else:
#         frequency[i]=1;
# print(frequency);

