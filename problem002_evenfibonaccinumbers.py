def even_fibonacci_numbers(n):
	a = fib(n);
	

	all_even_numbers = [a[x] for x in range(len(a)) if x % 3 == 0];

	sum_of_even_fib = sum(all_even_numbers);
	
	print("Fibbonaci Sequence: " + str(a));
	return sum_of_even_fib;

def fib(n):
	a = [0 , 1];

	for i in range(2,n):
		a.append(a[i-1]+a[i-2]);

	return a;


print("Sum: " + str(even_fibonacci_numbers(4)));
# Fibbonaci Sequence: [0, 1, 1, 2]
# Sum: 2

print("Sum: " + str(even_fibonacci_numbers(7)));
# Fibbonaci Sequence: [0, 1, 1, 2, 3, 5, 8]
# Sum: 10

print("Sum: " + str(even_fibonacci_numbers(10)));

# Fibbonaci Sequence: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# Sum: 44