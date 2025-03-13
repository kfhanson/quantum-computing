import numpy as np
import sympy
from sympy import symbols, cos, sin, I

def is_quantum_state(a, b):
  prob_0 = np.abs(a)**2 
  prob_1 = np.abs(b)**2
  tolerance = 1e-9 
  if np.isclose(prob_0 + prob_1, 1.0, atol=tolerance):
    return "yes"
  else:
    return "no"
  
def is_symbolic(a_str, b_str):
  try:
    theta = symbols('theta')
    a_expr = sympy.sympify(a_str)
    b_expr = sympy.sympify(b_str)
    if theta in a_expr.free_symbols or theta in b_expr.free_symbols:
      while True:
        try:
          theta_val = float(input("Enter a numerical value for theta (in radians): "))
          break
        except ValueError:
          print("Invalid value. Try again.")
      a_val = a_expr.evalf(subs={theta: theta_val})
      b_val = b_expr.evalf(subs={theta: theta_val})
    else:
      a_val = a_expr.evalf()
      b_val = b_expr.evalf()
    a = complex(a_val)
    b = complex(b_val)
    return is_quantum_state(a, b)
  except (SyntaxError, TypeError, ValueError) as e:
    print(f"Error: {e}")
    return "invalid"

while True:
  input_type = input("Enter (1) numerical values or (2) symbolic expressions? [1/2]: ")
  if input_type in ('1', '2'):
    break
  else:
    print("Choose 1 or 2. Try again")

if input_type == '1':
  while True:
    try:
      a_str = input("Input the value of a: ")
      a = complex(a_str)
      break
    except ValueError:
      print("Invalid input. Please enter a complex number (e.g., 0.707 + 0.707j).")

  while True:
    try:
      b_str = input("Input the value of b: ")
      b = complex(b_str)
      break 
    except ValueError:
      print("Invalid input. Please enter a complex number (e.g., 0.707 - 0.707j).")

  result = is_quantum_state(a, b)
  print(f"Is the vector ({a})|0> + ({b})|1> a quantum state? {result}")