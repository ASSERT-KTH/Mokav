def func(*args):
	ret_values = []
	
	from sys import stdin, stdout
	(n, m, a) = map(int, stdin.readline().rstrip().split())
	ret_values.append((((n // a) + bool((n % a))) * ((m // a) + bool((m % a)))))

	return ret_values
