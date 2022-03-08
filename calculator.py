# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def sub(n1, n2):
  return n1 - n2

# Multiply
def mul(n1, n2):
  return n1 * n2
  
# Divide
def div(n1, n2):
  return n1 / n2

# Calculate
def calculate(params):
  n1 = params[0]
  operation = params[1]
  n2 = params[2]
  
  if operation == '+':
    result = add(n1, n2)
  elif operation == '-':
    result = sub(n1, n2)
  elif operation == '*':
    result = mul(n1, n2)
  elif operation == '/':
    result = div(n1, n2)
  else:
    result = "Invalid input."
  return result

# Get input from user
def get_input(useOldn1):
  prompt1 = "What is your first number?\t"
  prompt2 = "What would you like to do? ( '+' '-' '*' '/' )\t"
  prompt3 = "What is your second number?\t"

  if useOldn1:
    n1 = 0
  else: 
    n1 = int(input(prompt1))
  operation = input(prompt2)
  n2 = int(input(prompt3))

  return [n1, operation, n2]