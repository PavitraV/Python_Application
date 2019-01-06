# Randomly fills an array of size 10x10 True and False, displayed as 1 and 0,
# and outputs the number chess knights needed to jump from 1s to 1s
# and visit all 1s (they can jump back to locations previously visited).

from itertools import product
from random import seed, randrange
import sys


dim = 10

def display_grid():
    for i in range(dim):
        print('     ', end = '')
        print(' '.join(grid[i][j] and '1' or '0' for j in range(dim)))
    print()

def explore_board():
	i = 0
	while i<len(x_list):
		y = knight_moves(x_list[i])
		if(x_list[i] in list1):
		    list1.remove(x_list[i])
		for p in y:
			if(p not in x_list):
				x_list.append(p)
				list1.remove(p)
		i+=1
	if(len(list1))!=0:
		list2.append('new knight')
		x_list.clear()
		y = knight_moves(list1[0])
		list1.remove(list1[0])
		for p in y:
			if(p not in x_list and p in list1):
				x_list.append(p)
		explore_board()
	return len(list2)
def knight_moves(position):
    x, y = position
    moves = list(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))
    moves = [(x,y) for x,y in moves if x >= 0 and y >= 0 and x < 10 and y < 10 and (x,y) in list1]
    return moves			

try:
    for_seed, n = (int(i) for i in input('Enter two integers: ').split())
    if not n:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
if n > 0:
    grid = [[randrange(n) > 0 for _ in range(dim)] for _ in range(dim)]
else:
    grid = [[randrange(-n) == 0 for _ in range(dim)] for _ in range(dim)]  

list1 = []
for row in range(len(grid)):
	for col in range(len(grid[0])):
		if(grid[row][col]):
			list1.append((row,col))

print('Here is the grid that has been generated:')
display_grid()
if(len(list1)==0):
	nb_of_knights = 0
else:
	x_list = []
	x = knight_moves(list1[0])
	for i in x:
		x_list.append(i)
	list1.remove(list1[0])
	list2 = []
	list2.append('new knight')
	nb_of_knights = explore_board()
if nb_of_knights== 0:
    print('No chess knight has explored this board.')
elif nb_of_knights == 1:
    print(f'At least 1 chess knight has explored this board.')
else:
    print(f'At least {nb_of_knights} chess knights have explored this board')

