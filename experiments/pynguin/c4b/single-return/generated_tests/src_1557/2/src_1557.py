def func(*args):
	
	from sys import stdin, stdout
	(n, m, a) = map(int, stdin.readline().rstrip().split())
	return((((n // a) + bool((n % a))) * ((m // a) + bool((m % a)))))
