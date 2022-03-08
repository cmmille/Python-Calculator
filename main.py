from calculator import *

continue_calcs = 'n'
calculator_running = True
while calculator_running:

  if continue_calcs == 'y':
    user_input = get_input(True)
    user_input[0] = result
  else:
    user_input = get_input(False)

  result = calculate(user_input)
  print(result)

  prompt0 = f"Would you like to continue calculating with {result}? (y/n) or ('q' to quit)\t"
  continue_calcs = input(prompt0).lower()
  if continue_calcs == 'q':
    calculator_running = False
