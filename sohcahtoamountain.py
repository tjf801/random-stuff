from math import *

G = int(input("GRID: "))

slopes = [[6, 2, "Slow Sam"], [5, 3, "Bobsled Bop"], [3, 3, "Daredevil Drop"], [6, 3, "Avalanche Alley"], [3, 5, "Thunder Run"], [14, 3, "Point E to point B   "]] 

def steepness(x, y):
	Gx = G*x
	Gy = G*y
	
	r = atan(Gy/Gx)
	return round(degrees(r), 2)

def rating(angle):
	if angle<30:
		return "Green"
	elif angle<45:
		return "Blue"
	else:
		return "Black"

def distance(x, y):
	return round(sqrt((G*x)**2 + (G*y)**2), 4)

def slant_height(d):
	angle = 62
	angle2 = 180 - 2*angle
	return d*sin(radians(angle))/sin(radians(angle2))

def height_eastern(alt):
	angledown = 41
	angleup = 27
	
	y = alt/tan(radians(angledown))
	x = y * tan(radians(angleup))
	
	return x

for i in range(len(slopes)):
	print("")
	s = steepness(slopes[i][0], slopes[i][1])
	print(slopes[i][2], s, rating(s), distance(slopes[i][0], slopes[i][1]))

#Q2
print("")
print("Trisha's run: ", distance(slopes[0][0], slopes[0][1])+distance(slopes[5][0], slopes[5][1])+distance(slopes[3][0], slopes[3][1]))

print("")
print("Chatlet slants:", slant_height(4))
print("Condo slants", slant_height(7.4))
print("")

A = int(input("ALTITUDE: "))

print("")
print("Difference of heights:", height_eastern(A))