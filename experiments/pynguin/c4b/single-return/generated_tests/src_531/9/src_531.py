def func(*args):
	
	numList = [int(x) for x in args[0].split()]
	listMax = 0
	listMin = 101
	for num in numList:
	    if (num > listMax):
	        listMax = num
	    if (num < listMin):
	        listMin = num
	numList.remove(listMax)
	numList.remove(listMin)
	minDistance = 300
	for num in range(listMin, listMax):
	    distance = ((abs((listMax - num)) + abs((numList[0] - num))) + abs((listMin - num)))
	    if (distance < minDistance):
	        minDistance = distance
	return(minDistance)
