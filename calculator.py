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

  calculation = {
    '+': add(n1, n2),
    '-': sub(n1, n2),
    '*': mul(n1, n2),
    '/': div(n1, n2)
  }
  result = calculation[operation]
  
  return result

# Get input from user
def get_input(useOldn1):
  prompt1 = "What is your first number?\t"
  prompt2 = "What would you like to do? ( '+' '-' '*' '/' )\t"
  prompt3 = "What is your next number?\t"

  if useOldn1:
    n1 = 0
  else: 
    n1 = float(input(prompt1))
  operation = input(prompt2)
  n2 = float(input(prompt3))

  return [n1, operation, n2]