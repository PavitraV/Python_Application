import sys
from random import seed, randrange


try:
    arg_for_seed = int(input('Enter an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
x = randrange(10 ** 10)
sum_of_digits_in_x = 0
L = [randrange(10 ** 8) for _ in range(10)]
first_digit_greater_than_last = 0
same_first_and_last_digits = 0
last_digit_greater_than_first = 0
distinct_digits = [0] * 9
min_gap = 10
max_gap = -1
first_and_last = set()

for i in str(x):
	sum_of_digits_in_x += int(i)

distinct_digits_list = []
first_last_list = []

distinct_digits = [0]*len(L)
for i in L:
	p = list(map(int,str(i)))
	q = len(p) - 1
	if(p[0]>p[q]):
		first_digit_greater_than_last += 1
	elif(p[0]==p[q]):
		same_first_and_last_digits += 1
	else : 
		last_digit_greater_than_first += 1
	distinct_digits_list.append(len(set(str(i))))
	gap = abs(p[0]-p[q])
	if(min_gap>gap):
		min_gap = gap
	if(max_gap<gap):
		max_gap = gap
	first_last_list.append((p[0],p[q]))

first_last_list = tuple(first_last_list)

p={}
j=0
for i in first_last_list:
	p[first_last_list[j]] = first_last_list.count(i)
	j+=1

maxval = max(p.values())
for i,j in p.items():
	if(j==maxval):
		first_and_last.add(i)
	
for i in distinct_digits_list:
	distinct_digits[i] += 1

print()
print('x is:', x)
print('L is:', L)
print()
print(f'The sum of all digits in x is equal to {sum_of_digits_in_x}.')
print()
print(f'There are {first_digit_greater_than_last}, {same_first_and_last_digits} '
      f'and {last_digit_greater_than_first} elements in L with a first digit that is\n'
      '  greater than the last digit, equal to the last digit,\n'
      '  and smaller than the last digit, respectively.'
     )
print()
for i in range(1, 9):
    if distinct_digits[i]:
        print(f'The number of members of L with {i} distinct digits is {distinct_digits[i]}.')
print()
print('The minimal gap (in absolute value) between first and last digits\n'
      f'  of a member of L is {min_gap}.'
     )
print('The maximal gap (in absolute value) between first and last digits\n'
      f'  of a member of L is {max_gap}.')
print()
print('The number of pairs (f, l) such that f and l are the first and last digits\n'
      f'of members of L is maximal for (f, l) one of {sorted(first_and_last)}.'
     )
        
