
def factorial(n: int) -> int:
	"""Return the factorial of a non-negative integer n."""
	if n < 0:
		raise ValueError("factorial() not defined for negative values")
	result = 1
	for i in range(2, n + 1):
		result *= i
	return result


if __name__ == "__main__":
	try:
		import sys
		if len(sys.argv) > 1:
			n = int(sys.argv[1])
		else:
			n = int(input("Enter non-negative integer: "))
		print(factorial(n))
	except Exception as e:
		print(e)
