def func(*args):
	ret_values = []
	
	integer = args[0]
	if (len(integer) > 1):
	    if ((len(set(integer[1:])) == 1) and (integer[(- 1)] == '9')):
	        ret_values.append(integer)
	    else:
	        needed_sum = sum([int(i) for i in integer])
	        sum_of_two = ((int(integer[0]) - 1) + 9)
	        pairs = []
	        for i in range(10):
	            for j in range(10):
	                if ((i + j) == sum_of_two):
	                    pairs.append([str(i), str(j)])
	        probable_integers = [int(''.join(([str((int(integer[0]) - 1))] + ['9' for _ in range((len(integer) - 1))])))]
	        for i in pairs:
	            for j in range(len(integer)):
	                for m in range((j + 1), len(integer)):
	                    result = ([str((int(integer[0]) - 1))] + ['9' for _ in range((len(integer) - 1))])
	                    result[j] = i[0]
	                    result[m] = i[1]
	                    probable_integers.append(int(''.join(result)))
	        probable_integers.append(int(integer))
	        probable_integers.sort()
	        a = probable_integers.index(int(integer))
	        if (needed_sum < sum([int(i) for i in str(probable_integers[(a - 1)])])):
	            ret_values.append(probable_integers[(a - 1)])
	        else:
	            ret_values.append(integer)
	else:
	    ret_values.append(integer)

	return ret_values
