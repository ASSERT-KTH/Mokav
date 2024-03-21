def func(*args):
	ret_values = []
	
	import sys
	import copy
	
	def checkAlmost(points):
	    for i in range(0, 3):
	        for moveDistance in [(- 1), 1]:
	            for axis in ['x', 'y']:
	                movedPoint = copy.deepcopy([points[i]])
	                remainPoint = (points[:i] + points[(i + 1):])
	                if (axis == 'x'):
	                    movedPoint[0][0] += moveDistance
	                else:
	                    movedPoint[0][1] += moveDistance
	                if ((movedPoint[0] == remainPoint[0]) or (movedPoint[0] == remainPoint[1]) or (remainPoint[0] == remainPoint[1])):
	                    continue
	                if (checkRight((movedPoint + remainPoint)) == True):
	                    return True
	    return False
	
	def checkRight(points):
	    if ((points[0] == points[1]) or (points[1] == points[2]) or (points[0] == points[2])):
	        return False
	    distancs = []
	    distancs.append(getDistance(points[0], points[1]))
	    distancs.append(getDistance(points[0], points[2]))
	    distancs.append(getDistance(points[1], points[2]))
	    distancs.sort()
	    if ((distancs[0] + distancs[1]) == distancs[2]):
	        return True
	    else:
	        return False
	
	def getDistance(point1, point2):
	    x_diff = (point1[0] - point2[0])
	    y_diff = (point1[1] - point2[1])
	    return ((x_diff * x_diff) + (y_diff * y_diff))
	
	def solve(firstLine):
	    points = [[firstLine[0], firstLine[1]], [firstLine[2], firstLine[3]], [firstLine[4], firstLine[5]]]
	    if (checkRight(points) == True):
	        ret_values.append('RIGHT')
	    elif (checkAlmost(points) == True):
	        ret_values.append('ALMOST')
	    else:
	        ret_values.append('NEITHER')
	    return
	
	def main():
	    firstLine = sys.stdin.readline().split()
	    firstLine = list(map(int, firstLine))
	    solve(firstLine)
	if (__name__ == '__main__'):
	    main()

	return ret_values
