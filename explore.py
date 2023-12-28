print("\n----- creating a list of integers -----")
# noob
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("noob nums:", nums)

# better
nums = []
for i in range(1, 11):
    nums.append(i)
print("better nums:", nums)

# pro!
nums = [i for i in range(1,11)]
print("pro nums:", nums)



print("\n----- looping through each item -----")
import random
nums = [random.randint(1,100) for i in range(100)]
count_teens = 0
for num in nums:
    if num > 12 and num < 20:
        count_teens += 1
print("this many numbers in the 'teens':", count_teens)
