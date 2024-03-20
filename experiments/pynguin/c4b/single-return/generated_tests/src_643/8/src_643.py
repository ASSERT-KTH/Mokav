def func(*args):
	
	
	def main():
	    (x, t, a, b, da, db) = map(int, args[0].split())
	    db *= (- 1)
	    tdb = (t * db)
	    s = {z for y in range((a + b), ((a + b) - (da * t)), (- da)) for z in range(y, (y + tdb), db)}
	    s.update(range(a, (a - (da * t)), (- da)))
	    s.update(range(b, (b + tdb), db))
	    s.add(0)
	    return(('NO', 'YES')[(x in s)])
	if (__name__ == '__main__'):
	    main()
