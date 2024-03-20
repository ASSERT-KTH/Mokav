def func(*args):
	
	from sys import stdin
	import math
	(n, m, k, x, y) = map(int, stdin.readline().rstrip().split())
	tour_size = ((((2 * n) * m) - (2 * m)) if (n > 1) else m)
	max_asked_per_tour = (2 if (n >= 3) else 1)
	min_asked_per_tour = 1
	last_tour_count = (k % tour_size)
	max_asked = max((((k // tour_size) * max_asked_per_tour) + (0 if (last_tour_count <= m) else (1 if (m < last_tour_count <= (m * n)) else 2))), math.ceil((k / tour_size)))
	min_asked = (((k // tour_size) * min_asked_per_tour) + (1 if (last_tour_count >= (n * m)) else 0))
	asked_per_tour = (2 if (1 < x < n) else 1)
	pre_tour_pos = (((x - 1) * m) + y)
	pos_tour_pos = ((- 1) if (asked_per_tour == 1) else (((m * n) + (((n - x) - 1) * m)) + y))
	last_pre_tour_asked = (0 if ((k % tour_size) < pre_tour_pos) else 1)
	last_pos_tour_asked = (0 if ((pos_tour_pos == (- 1)) or ((k % tour_size) < pos_tour_pos)) else 1)
	sergei_asked = ((((k // tour_size) * asked_per_tour) + last_pre_tour_asked) + last_pos_tour_asked)
	return(' '.join(map(str, [max_asked, min_asked, sergei_asked])))
