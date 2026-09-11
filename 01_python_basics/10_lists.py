# append()
# Adds an element to the end
# arr=[10,20,30];
# arr.append(40);
# print(arr);

# insert()
# Insert at a specific index
# arr=[10,20,30];
# arr.insert(1,99);
# print(arr);

# remove()
# Remove the first occurence of a value
# arr=[10,20,30,40];
# arr.remove(20);
# print(arr);

# pop()
# Removes an element using its index
# arr=[10,20,30,40];
# x=arr.pop(2);
# print(x);
# print(arr);

# Searching (in)
# arr=[10,20,30,40];
# print(30 in arr);

# Traversing a List:
# arr=[10,20,30];
# for i in arr:
#     print(i);

# sort():
# Ascending=
# arr=[5,2,8,1,3];
# arr.sort();
# print(arr);

# Descending=
# arr=[5,2,8,1,3];
# arr.sort(reverse=True);
# print(arr);

# reverse():
# arr=[1,2,3,4];
# arr.reverse()
# print(arr);

# len():
# arr=[10,20,30];
# print(len(arr));

# Nested Lists:

# ex:
# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(matrix[0][1]);

# Q1
# arr=[10,20,30,40,50];
# arr[2]=100;
# print(arr);

# Q2
# arr=[10,20,30];
# arr.append(40);
# arr.append(50);
# print(arr);

# Q3
# arr=[10,20,30,40];
# arr.insert(2,25);
# print(arr);

# Q4
# arr=[10,20,30,20,40];
# arr.remove(20);
# print(arr);

# Q5
# arr=[5,10,15,20,25];
# for i in range(len(arr)):
#     if arr[i]==15:
#         print("Found at Index:",i);

# Q6
# arr=[10,20,30,40,50];
# sum=0;
# for i in arr:
#     sum+=i;
# print(sum);

# Q7
# arr=[12,5,8,20,3,15];
# minimum=arr[0];
# for i in arr:
#     if i<minimum:
#         minimum=i;
# print("Minimum:",minimum);

# Q8
# it will print [1,2,3] and [1,2,3] because they are not independent if changes apply to one then automatically apply to other.