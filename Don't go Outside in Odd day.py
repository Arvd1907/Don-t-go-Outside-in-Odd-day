# Write a Python program to count the number of even and odd numbers from a series of numbers.

count_even = 0
count_odd = 0
for i in range(1,20):
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print(count_odd)
print(count_even)