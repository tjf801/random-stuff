p = [[2,3], [-4,5], [1,0], [-2,1], [3,-2], [7,0], [-5,-1]]

#Bubble sort on p
for j in range(len(p)):
	for i in range(len(p) - 1):
		d1 = (p[i][0] ** 2) + (p[i][1] ** 2) #distance to point 1
		d2 = (p[i+1][0] ** 2) + (p[i+1][1] ** 2) #distance to point 2
		if d1>d2:
			#swaps them if they are in the wrong order
			a = p[i]
			p[i] = p[i+1]
			p[i+1] = a

x = int(input())
for i in range(x):
	print(p[i])