def func(*args):
	
	n = int(args[0])
	strstone = args[1]
	stones = []
	for i in strstone:
	    stones.append(i)
	to_remove = 0
	position = 0
	while (position < len(stones)):
	    stone = stones[position]
	    if (len(stones) == 1):
	        break
	    elif (position == 0):
	        if (stones[(position + 1)] == stone):
	            to_remove += 1
	            stones.pop(position)
	            position -= 1
	    elif (position == (len(stones) - 1)):
	        if (stones[(position - 1)] == stone):
	            to_remove += 1
	            stones.pop(position)
	            position -= 1
	    elif (stones[(position + 1)] == stone):
	        to_remove += 1
	        stones.pop(position)
	        position -= 1
	    elif (stones[(position - 1)] == stone):
	        to_remove += 1
	        stones.pop(position)
	        position -= 1
	    position += 1
	return(to_remove)
