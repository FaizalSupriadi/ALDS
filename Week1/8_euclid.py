def gcd( q, p ):
	if p > q:
		return gcd(p, q)
	if q % p == 0:
		return p
	return gcd(p, q%p)

print(gcd(12, 8))