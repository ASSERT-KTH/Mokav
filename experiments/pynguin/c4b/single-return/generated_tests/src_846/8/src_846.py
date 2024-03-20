def func(*args):
	
	import math
	import copy
	numbers = [int(x) for x in args[0].split(' ')]
	ribbon_length = numbers[0]
	pieces = numbers[1:]
	pieces = list(set(pieces))
	pieces.sort()
	result = set()
	for i in range(len(pieces)):
	    number = pieces[i]
	    temp_list = copy.copy(pieces)
	    temp_list.pop(i)
	    if ((ribbon_length % number) == 0):
	        result.add(int((ribbon_length / number)))
	    else:
	        estimation = int(math.floor((ribbon_length / number)))
	        for j in range(1, estimation):
	            lack = (ribbon_length - (number * (estimation - j)))
	            if (lack > 0):
	                for k in range((len(pieces) - 1)):
	                    if ((lack % temp_list[k]) == 0):
	                        result.add(((estimation - j) + int((lack / temp_list[k]))))
	                if (len(pieces) == 3):
	                    for x in range(1, (j + 1)):
	                        lack = (lack - (temp_list[0] * x))
	                        if (lack > 0):
	                            if ((lack % temp_list[1]) == 0):
	                                result.add((((estimation - j) + x) + int((lack / temp_list[1]))))
	return(max(result))
