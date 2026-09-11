# Creating a String
# name="Arman";

# Indexing
# s="python";
# print(s[0]);
# print(s[1]);
# print(s[2]);

# Negative Indexing:
# s="python";
# print(s[-1]);
# print(s[-1]);

# Slicing
# Remember: Start Included, Stop Excluded
# s[start:stop]

# s="python";
# print(s[0:3]);

# Reverese a String:
# s="python"
# print(s[::-1]);

# len():
# s="python";
# print(len(s));

# Loop through a String:
# s="python";
# for ch in s:
#     print(ch);

# or using indexes:
# s="python";
# for i in range(len(s)):
#     print(s[i]);

# Check Character with in:
# s="python";
# print("p" in s);
# print("z" in s);

# lower() and upper():
# s="python"
# print(s.lower());
# print(s.upper());

# split()
# s="10 20 30 40";
# arr=s.split();
# print(arr);

# join():
# arr=['10','20','30'];
# r=",".join(arr);
# print(r);

# DSA ex:
# Count Characters
# s="banana";
# target="a";
# count=0;
# for ch in s:
#     if ch==target:
#         count+=1;
# print(count);

# DSA ex:
# Palindrome:
# s="madam";
# if s==s[::-1]:
#     print("Plaindrome");
# else:
#     print("Not Palindrome");

# Q1
# s="Hello";
# print(len(s));

# Q2
# s="Hello";
# print("First Character:", s[0]);
# print("Last Character:", s[-1]);

# Q3
# s="python";
# for i in s:
#     print(i);

# Q4
# s="banana";
# count=0;
# for i in s:
#     if i=='a':
#         count+=1;
# print(count);

# Q5
# s="hello";
# print(s[::-1]);

# Q6
# s="level";
# if s==s[::-1]:
#     print("Palindrome");
# else:
#     print("Not Palindrom");

# Q7
# s="Python Programming";
# count=0;
# for i in s:
#     if i==" ":
#         count+=1;
# print(count);

# Q8
# s = "Python Programming";
# print(s[1:4]);
# print(s[1:4:2])
