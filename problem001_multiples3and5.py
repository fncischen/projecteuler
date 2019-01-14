import math

def sum_of_multiples_of_three_and_five_below(number):
	# floor the number after division by 3 & 5, to see
	# how many times are needed to get 

	a = math.floor((number-1)/3);
	b = math.floor((number-1)/5);

	c = math.floor((number-1)/15);

	d = 3 * sum_natural_numbers(a) + 5 * sum_natural_numbers(b) - 15 * sum_natural_numbers(c); 

	return d;

def sum_natural_numbers(n):
	if n == 0:
		return 0;
	else:
		return n * ( n + 1) / 2;

# test for small numbers
print(sum_of_multiples_of_three_and_five_below(10));
print(sum_of_multiples_of_three_and_five_below(12));
print(sum_of_multiples_of_three_and_five_below(15));

# there are edge cases where we don't want to
# double count numbers which are both multiples of 3 and 5 - i.e multiples of 15.  
print(sum_of_multiples_of_three_and_five_below(19));

# test for big numbers 
print(sum_of_multiples_of_three_and_five_below(1000));