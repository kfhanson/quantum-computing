import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import circuit_drawer

qc = QuantumCircuit(2, name="Reversible Circuit")
print("Applying forward operations (Steps 1-5)...")
qc.h(0)
qc.x(1)
qc.tdg(1)
qc.cx(1, 0)
angle = -np.pi / 3
qc.p(angle, 0)

qc.barrier(label="U | U†")
print("Applying reverse operations (Step 6)...")
qc.p(-angle, 0)
qc.cx(1, 0)
qc.t(1)
qc.x(1)
qc.h(0)

print("\nDrawing the circuit...")
print(qc.draw('text'))

print("\nVerifying the final state using simulation...")

statevector_simulator = AerSimulator(method='statevector')
sim_qc = qc.copy()
sim_qc.save_statevector()
job_statevector = statevector_simulator.run(sim_qc) # No need for execute
result_statevector = job_statevector.result()

output_state = result_statevector.get_statevector(sim_qc, decimals=3)
print("\nFinal State Vector:")
print(output_state)

if np.allclose(output_state.data, [1, 0, 0, 0]):
    print("Verification Successful: Final state is |00>")
else:
    print("Verification Failed: Final state is NOT |00>")