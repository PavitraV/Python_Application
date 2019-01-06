from random import seed, randrange
import sys
import numpy as np


dim = 10


def display_grid():
    for i in range(dim):
        print('     ', end = '')
        print(' '.join(f'{int(e)}' for e in grid[i]))
    print()


# If j1 <= j2 and the grid has a 1 at the intersection of row i and column j
# for all j in {j1, ..., j2}, then returns the number of blocks in the construction
# built over this line of blocks.
        
try:
    for_seed, n = input('Enter two integers, the second one being strictly positive: ').split()
    for_seed = int(for_seed)
    n = int(n)
    if n <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[bool(randrange(n)) for _ in range(dim)] for _ in range(dim)]
n = len(grid[0])
max_count = 0
print('Here is the grid that has been generated:')
display_grid()

grid_num = [[0]*n for x in range(n)]

for i in range(len(grid)):
	for j in range(n):
		if(grid[i][j]):
			grid_num[i][j] = 1
		else:
			grid_num[i][j] = 0
grid_num = grid_num[::-1]

grid_num = np.array(grid_num)
grid_num = grid_num.transpose()

for i in range(len(grid_num)):
	for j in range(1,n):
		if(grid_num[i][-(j+1)]!=0):
			grid_num[i][-(j+1)] = grid_num[i][-(j+1)] +grid_num[i][-j]

for i in range(dim):
	print('     ', end = '')
	print(' '.join(f'{int(e)}' for e in grid_num[i]))
print()
grid_num = grid_num.transpose()

for i in range(n):
	for j in range(n-1):
		if(grid_num[i][j+1]!=0 and grid_num[i][j]!=0):
			grid_num[i][j+1] = grid_num[i][j+1] +grid_num[i][j]

size = max(grid_num.flatten())

if not size:
    print(f'The largest block construction has no block.')  
elif size == 1:
    print(f'The largest block construction has 1 block.')  
else:
    print(f'The largest block construction has {size} blocks.')  
