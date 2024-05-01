def patched_func(*args):
	global_list = []
	
	
	def max_score(n):
	    max_score = 0
	    any_choice = False
	    for i in range(0, (len(n) - 2)):
	        for j in range((i + 1), (len(n) - 1)):
	            if (((n[:(i + 1)][0] == '0') and (len(n[:(i + 1)]) > 1)) or ((n[(i + 1):(j + 1)][0] == '0') and (len(n[(i + 1):(j + 1)]) > 1)) or ((n[(j + 1):][0] == '0') and (len(n[(j + 1):]) > 1)) or (int(n[:(i + 1)]) > 1000000) or (int(n[(i + 1):(j + 1)]) > 1000000) or (int(n[(j + 1):]) > 1000000)):
	                continue
	            else:
	                any_choice = True
	            new_score = ((int(n[:(i + 1)]) + int(n[(i + 1):(j + 1)])) + int(n[(j + 1):]))
	            if (new_score > max_score):
	                max_score = new_score
	    if any_choice:
	        return max_score
	    else:
	        return (- 1)
	
	def main():
	    allscores = args[0]
	    global_list.append(max_score(allscores))
	main()
	return global_list