'''
Without using any string methods, try to print the following:
123...n
Note that "..." represents the consecutive values in between.
Example
n = 5
Prints the string 12345
'''

n = int(input("Enter an integer: "))
for i in range(n):
    print(i+1, end='')  # end='' argument prevents the print() function from adding a newline after each number.
