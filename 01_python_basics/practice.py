# SET-1:-

# Q1
# a = [i * i for i in range(1,11)]
# print(a)

# Q2
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# a = [i for i in nums if i % 2 == 0]
# print(a)

# Q3
# a = {i: i * i for i in range(1, 6)}
# print(a)

# Q4
# nums = [1, 2, 2, 3, 3, 4, 5]
# a = {i * i for i in nums}
# print(a)

# Q5
# nums = [1, 2, 3, 4, 5]
# a = ["Even" if i % 2 == 0 else "Odd" for i in nums]
# print(a)

# Q6
# word = "Python"
# a = [i for i in word.upper()]
# print(a)

# Q7
# names = ["Arman", "Rahul", "Jay"]
# a = {n: len(n) for n in names}
# print(a)

# Q8
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a = [i * i if i % 2 == 0 else i * i * i for i in nums]
# print(a)

# Q9
# [6,8,10]

# Q10
# {2:4,4:16}


# SET-2:-

# Q1
# [2,6,10]

# Q2
# [10,2,30,4,50]

# Q3
# nums = [1, 2, 3, 4, 5]
# result = [x * 2 for x in nums if x % 2 == 0]
# print(result)

# Q4
# {1,2,3,4}

# Q5
# nums = [1, 2, 3, 4, 5]
# a = {i:"Even" if i % 2 == 0 else "Odd" for i in nums}
# print(a)

# Q6
# {'p','y','t','h','o','n'}

# Q7
# nums = [2, 5, 8, 11, 14, 17]
# a = [i * 2 for i in nums if i % 2 == 0]
# print(a)

# Q8
# [11,21,12,22]

# Q9
# {1: "Odd", 2: "Even", 3: "Odd", 4: "Even"}

# Q10
# 16


# SET:-3

# Q1
# error because there should be and between two if

# Q2
# [10,20,6,8]

# Q3
# {2:4,4:8}

# Q4
# O

# Q5
# {4,8}

# Q6
# [0,3,2]

# Q7
# nums = [1, 2, 3, 4, 5]
# result = [x * x for x in nums if x > 0]
# print(result)

# Q8
# {1:1,2:4,3:9,4:16}

# Q9
# heo

# Q10
# {3:27,4:16,5:125,6:36}


# SET:-4

# Q1
# nums = [4, 7, 2, 7, 9, 2, 5]
# a = [i for i in nums if i > 4 if i % 2 == 1]
# print(a)

# Q2
# word = "programming"
# a = word[::-1]
# print(a)

# Q3
# marks = {"Math": 85, "Python": 92, "DBMS": 78, "DSA": 95}
# a = {subject: score for subject, score in marks.items() if score >= 80}
# print(a)

# Q4
# nums = [10, 20, 30, 40, 50]
# maxi = nums[0]
# for i in nums:
#     if i > maxi:
#         maxi = i
# print(maxi)

# Q5
# nums = [18, 5, 27, 3, 12]
# mini = nums[0]
# for i in nums:
#     if i < mini:
#         mini = i
# print(mini)

# Q6
# nums = [12, 7, 4, 9, 16, 3, 8]
# even = 0
# odd = 0
# for i in nums:
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(even, odd)

# Q7
# nums = [4, 2, 4, 7, 2, 9, 7, 1]
# a = []
# for i in nums:
#     if i not in a:
#         a.append(i)
# print(a)

# Q8
# nums = [10, 5, 20, 8, 20, 15]
# a = 0
# b = 0
# for i in nums:
#     if i > a:
#         b = a
#         a = i
#     elif i > b and i != a:
#         b = i
# print(b)

# Q9
