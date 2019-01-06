import sys
from random import seed, randint
from math import gcd,sqrt

try:
    arg_for_seed, length, max_value = input('Enter three strictly positive integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 1 or length < 1 or max_value < 1:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(1, max_value) for _ in range(length)]
print('Here is L:')
print(L)
print()

size_of_simplest_fraction = 2
simplest_fractions = []
size_of_most_complex_fraction = 0
most_complex_fractions = []
multiplicity_of_largest_prime_factor = 0
largest_prime_factors = []

# REPLACE THIS COMMENT WITH YOUR CODE
simplest_fractions.append((1,1))

def sieve_of_primes_up_to(n):
    sieve = [True] * (n + 1)
    for p in range(2, round(sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return (p for p in range(2,len(sieve)-1) if sieve[p])

def primefactors(n):
	primes = sieve_of_primes_up_to(n+1)
	factors = {}
	for i in primes:
		while n%i == 0:
			n = n// i
			if(not i in factors):
				factors[i] = 1
			else:
				factors[i] += 1
			
	return factors	
newlist = []
for i in L:
	for j in L:
		num,deno = i,j
		if(num <= deno):
			newlist.append((num//gcd(num,deno), deno//gcd(num,deno)))

maxlen = max(len(str(i))+len(str(j)) for i,j in newlist)
size_of_most_complex_fraction = maxlen
for i,j in newlist:
	num, deno = i,j
	l1 = len(str(num))
	l2 = len(str(deno))
	if(l1+l2 == 2 and (num,deno) not in simplest_fractions):
		simplest_fractions.append((num,deno))
	if(l1+l2 == maxlen and (num,deno) not in most_complex_fractions):
		most_complex_fractions.append((num,deno))

simplest_fractions =  sorted(simplest_fractions, key = lambda x : x[0]/x[1])
most_complex_fractions =  sorted(most_complex_fractions, reverse = True, key = lambda x : x[0]/x[1])

multiplicity = []
for i in most_complex_fractions:
	multiplicity.append(primefactors(i[1]))

if(multiplicity== [{}]):
	multiplicity_of_largest_prime_factor = 0

else:
	multiplicity_of_largest_prime_factor = max(prime[key] for prime in multiplicity for key in prime)
	for i in multiplicity:
		for key in i:
			if(i[key] == multiplicity_of_largest_prime_factor and key not in largest_prime_factors):
				largest_prime_factors.append(key)

			
largest_prime_factors = sorted(largest_prime_factors)	

print('The size of the simplest fraction <= 1 built from members of L is:',
      size_of_simplest_fraction
     )
print('From smallest to largest, those simplest fractions are:')
print('\n'.join(f'    {x}/{y}' for (x, y) in simplest_fractions))
print('The size of the most complex fraction <= 1 built from members of L is:',
      size_of_most_complex_fraction
     )
print('From largest to smallest, those most complex fractions are:')
print('\n'.join(f'    {x}/{y}' for (x, y) in most_complex_fractions))
print("The highest multiplicity of prime factors of the latter's denominators is:",
      multiplicity_of_largest_prime_factor
     )
print('These prime factors of highest multiplicity are, from smallest to largest:')
print('   ', largest_prime_factors)
