def func(*args):
	
	(a, t_a) = map(int, args[0].split())
	(b, t_b) = map(int, args[1].split())
	(h, m) = map(int, args[2].split(':'))
	time = ((h * 60) + m)
	start = time
	end = ((time + t_a) - 1)
	start_time = 300
	end_time = ((start_time + t_b) - 1)
	intersections = 0
	while (start_time <= 1439):
	    if ((end >= start_time) and (end_time >= start)):
	        intersections += 1
	    start_time += b
	    end_time = ((start_time + t_b) - 1)
	yield(intersections)
