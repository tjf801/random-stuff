size = int(input('size: '))
sqlen = size**2
import copy


"""
grid = [
	[ 0, 0, 0, 0, 1, 0, 0, 4, 6, 9, 0, 0, 0, 2, 0,12], 
	[ 3, 9, 0, 5, 0,15,10, 0, 0, 0,11,12,13, 7, 8, 0], 
	[ 0, 0, 0, 0, 0, 3, 6, 0,13, 0, 0,16,15, 0, 9,11], 
	[ 0, 0, 0,16, 0, 0, 0,11, 0, 0,10,15,14, 6, 0, 0], 
	[ 0, 0, 2, 7, 0, 8, 0, 5,16, 0,12,13,11, 1, 0, 0], 
	[ 0, 0, 0, 0, 4, 0,14, 7, 3,10, 0, 0, 9,12, 0, 8], 
	[10, 0, 9,12, 0, 1,11, 6,14, 8, 0, 0, 0, 0, 0, 7], 
	[ 0,11, 0, 8,10, 0,13, 0, 9, 0, 1, 0, 3, 0, 6,15], 
	[13, 8, 0, 2, 0, 0, 0, 0,15,12, 5, 0, 4, 0, 0, 3], 
	[15, 0, 0, 4, 2, 0, 5, 3,11,14, 0, 1, 6, 8, 7, 9], 
	[ 0,14, 3, 6,11, 0,16,10, 0, 0, 0, 9, 0,15, 0, 0], 
	[ 5, 0,16, 0, 0, 0, 0, 0, 2, 4, 0,10, 1,11,13, 0], 
	[ 9,16,14,13, 0,10, 2, 0, 7, 0, 0, 4, 0, 5, 0, 0], 
	[ 6, 0, 0, 0,12, 5,15,14, 0, 0, 0, 0, 8, 0, 0, 0], 
	[ 0, 0, 4, 0, 6, 0, 9, 1, 0, 0,13, 0,10, 3,16, 2], 
	[12, 1, 0, 0, 0, 0, 4, 0,10, 5, 2, 8, 0, 0,14, 0],
	]
"""
grid = [
	[0, 3, 0, 0, 7, 0, 5, 9, 6], 
	[4, 7, 6, 0, 0, 0, 0, 1, 0], 
	[0, 0, 2, 0, 1, 8, 7, 4, 0], 
	[5, 0, 0, 3, 2, 6, 0, 0, 4], 
	[2, 8, 0, 0, 0, 0, 0, 6, 1], 
	[3, 0, 0, 1, 8, 9, 0, 0, 7], 
	[0, 2, 8, 4, 5, 0, 1, 0, 0], 
	[0, 4, 0, 0, 0, 0, 6, 2, 8], 
	[1, 9, 3, 0, 6, 0, 0, 7, 0]
	]


def getgrid(file):
	sudoku = open(file, "r")
	g = []
	for i in range(sqlen):
		a = []
		for j in range(sqlen+1):
			x = sudoku.readline(1)
			if x=='': continue
			if (x[0] == 0):
				x = x.lstrip('0')
			if (str(x)!='\n'):
				x = x.rstrip('.')
				a.append(char_to_number(x))
		g.append(a)
	return g

def get_allowed_values(s):
	allowed_values = []
	for i in range(s**2):
		line = []
		for j in range(s**2):
			box = [k+1 for k in range(s**2)]
			line.append(box)
		allowed_values.append(line)
	return allowed_values

def eliminateallvals():
	#Gets rid of the allowedvalues already in grid
	for i in range(sqlen):
		for j in range(sqlen):
			if (grid[i][j] != 0):
				for k in range(sqlen):
					allowedvalues[i][j][k] = 0

def eliminatecolrow():
	for i in range(sqlen):
		for j in range(sqlen):
			#repeats what is in HERE for every number in grid
			#Eliminates things in columns
			for k in range(sqlen):
				for l in range(sqlen):
					if(grid[i][l] == (k+1)):
						#print("Eliminated column value " + str(k+1) + " at " + str(i) + " " + str(j))
						allowedvalues[i][j][k] = 0
			for k in range(sqlen):
				for l in range(sqlen):
					if(grid[l][j] == (k+1)):
						#print("Eliminated row value " + str(k+1) + " at " + str(i) + " " + str(j))
						allowedvalues[i][j][k] = 0

def eliminatebox():
	for i in range(sqlen):
		for j in range(sqlen):
			if(grid[i][j] != 0):
				a = grid[i][j] - 1
				for m in range(size):
					for n in range(size):
						allowedvalues[(m+i-(i%size))][(n+j-(j%size))][a] = 0

def placevalues():
	for i in range(sqlen):
		for j in range(sqlen):
			a = 0
			b = 0
			for k in range(sqlen):
				if(allowedvalues[i][j][k] != 0):
					a = a + 1
					b = k
			if (a == 1):
				grid[i][j] = allowedvalues[i][j][b]
				allowedvalues[i][j][b] = 0

def print_grid(grid):
	for i in range(sqlen):
		line = ""
		for j in range(sqlen):
			line += number_to_char(str(grid[i][j])) + " "
		print(line)

def number_to_char(strnum):
	if len(strnum)==1: return strnum
	else: return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[int(strnum)-10]

def char_to_number(char):
	try: return int(char)
	except: return ord(char)-55

def check_solved(grid):
	for i in range(sqlen):
		for j in range(sqlen):
			if grid[i][j]==0: return False
	return True

grid = getgrid("4x4Easy1.txt")

allowedvalues = get_allowed_values(size)
print_grid(grid)
i = 0
while not check_solved(grid):
	i += 1
	previousgrid = copy.deepcopy(grid)
	eliminateallvals()
	eliminatecolrow()
	placevalues()
	eliminateallvals()
	eliminatebox()
	placevalues()
	#if input()=="y": 
	#	print(previousgrid==grid)
	#	print_grid(grid)
print("")
print_grid(grid)
print("")
print("took " +str(i)+ " iterations")