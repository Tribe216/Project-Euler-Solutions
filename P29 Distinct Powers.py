def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
				
def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac		
	
def listSame(lst):
       return lst[1:] == lst[:-1]	
	   
def validateUniqueness(basenum,factor):
	if listSame(primes(basenum)) and basenum not in primes(basenum):
		if((len(primes(basenum)) * factor) <= 100):
			return 0
	return 1
	   
counter = 0
for x in range(2,101):
	for y in range(2,101):
		#print x,y,validateUniqueness(x,y)
		counter += int(validateUniqueness(x,y))
		
print counter


	