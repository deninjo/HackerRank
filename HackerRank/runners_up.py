'''
xx = [1, 5, 4, 6, 6]
xx = list(set(xx))
xx.sort()
print(xx)
print(xx[-2])
'''

n = int(input("How many elements: "))
# arr = map(int, input("Enter elements: ").split())  # applies the int to each element
# arr = list(arr)
arr = input("Enter elements: ")
arr = [int(x) for x in arr.split()]

if len(arr) == n:
    arr = list(set(arr))
    arr.sort()
else:
    print("Number of elements does not equal n")

print(arr[-2])




