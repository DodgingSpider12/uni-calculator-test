def add(a,b):
	return a + b

def subtract(a,b):
	return a - b

def multiply(a,b):
	return a*b

def division(a,b):
	return a / b

def main():
	while True:
		firstNum = float(input("enter first number please"))
		operator = input("enter operator (+, -, *, /")
		secondNum = float(input("enter second number please"))
		if operator == "+":
			print("result", add(firstNum, secondNum))
		elif operator == "-":
			print("result", subtract(firstNum, secondNum))
		elif operator == "*":
			print("result", multiply(firstNum, secondNum))
		elif operator == "/":
			print("result", division(firstNum, secondNum))
		else:
			print("Unknown operator", operator)

if __name__== "__main__":
	main()
