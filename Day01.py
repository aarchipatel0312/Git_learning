def calculate(first, operator, second):
	if operator == "+":
		return first + second
	if operator == "-":
		return first - second
	if operator == "*":
		return first * second
	if operator == "/":
		if second == 0:
			raise ZeroDivisionError("Cannot divide by zero.")
		return first / second
	raise ValueError("Unsupported operator. Use +, -, *, or /.")


def main():
	try:
		first = float(input("First number: "))
		operator = input("Operator (+, -, *, /): ").strip()
		second = float(input("Second number: "))
		print("Result:", calculate(first, operator, second))
	except (ValueError, ZeroDivisionError) as error:
		print("Error:", error)


if __name__ == "__main__":
	main()

print("This is a simple calculator program. You can perform addition, subtraction, multiplication, and division.")