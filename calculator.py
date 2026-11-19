def add(a,b):
	return a + b

def subtract(a,b):
	return a - b

def multiply(a,b):
	return a+b # deliberately wrong

def divide(a,b):
	return a / b

def circleArea(r):
	if r  >= 0:
		return 3.14 * r * r
	else:
		return "Error"

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
			print("result", divide(firstNum, secondNum))
		else:
			print("Unknown operator", operator)

if __name__== "__main__":
	main()
