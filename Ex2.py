import math
list_ = []
count = 0
sum = 0
while count < 10:
    try:
        n = int(input("Number:"))
        list_.append(n)
        count += 1
        sum += n
    except ValueError:
        print("It is not a number")

list_.sort()
print(f"The maximum: {max(list_)}")
print(f"The minimum: {min(list_)}")
print(f"The arithmetic mean: {sum/count}")
print(f"The median: {list_[count//2 + 1]}")