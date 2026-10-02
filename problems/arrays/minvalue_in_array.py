a=[3,2,34,756,1,3,54,23,4,5,6,7,8,9,10]
min_value = min(a)
max_value = max(a)
for i in range(len(a)):
    if a[i] < min_value:
        min_value = a[i]
    if a[i] > max_value:
        max_value = a[i]
print("The minimum value in the array is:", min_value)
print("The maximum value in the array is:", max_value)