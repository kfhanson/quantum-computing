import numpy as np

def is_quantum_state(a, b):
  prob_0 = np.abs(a)**2 
  prob_1 = np.abs(b)**2
  tolerance = 1e-9 
  if np.isclose(prob_0 + prob_1, 1.0, atol=tolerance):
    return "yes"
  else:
    return "no"

while True:
  try:
    a_str = input("Input the value of a (e.g., 0.707 + 0.707j): ")
    a = complex(a_str)
    break
  except ValueError:
    print("Invalid input for a. Please enter a complex number (e.g., 0.707 + 0.707j).")

while True:
  try:
    b_str = input("Input the value of b (e.g., 0.707 - 0.707j): ")
    b = complex(b_str)
    break 
  except ValueError:
    print("Invalid input for b. Please enter a complex number (e.g., 0.707 - 0.707j).")


result = is_quantum_state(a, b)
print(f"Is the vector ({a})|0> + ({b})|1> a quantum state? {result}")