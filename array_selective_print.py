"""Input upper and lower limit for a pre-defined array in a list and print the elements within that bracket"""

print('Enter the upper limit = ',end='')
upper=int(input())
print('Enter the lower limit = ',end='')
lower=int(input())

lst=[1,34,23,1,2,4,34,6,4,5335,34,34,76,1,4,8,0,5]

print('List elements within the mentioned limits are mentioned below :')

for item in lst:
    if item>=lower and item<=upper:
        print(item,end=',')
