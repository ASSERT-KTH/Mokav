def func(*args):
	
	numbers = list(map(int, args[0].split()))
	sum = 0
	count = []
	for i in range(0, 101):
	    count.append(0)
	for number in numbers:
	    count[number] += 1
	    sum += number
	current_sum = sum
	for number in numbers:
	    if (count[number] >= 2):
	        if (count[number] >= 3):
	            multiply = 3
	        else:
	            multiply = 2
	        if ((sum - (number * multiply)) < current_sum):
	            current_sum = (sum - (number * multiply))
	return(current_sum)
