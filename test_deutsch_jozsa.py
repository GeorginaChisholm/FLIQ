# Python test file

from qiskit import Aer, execute
from deutsch_jozsa_tutorial import deutsch_jozsa_circuit, constant_oracle, balanced_oracle

def test_algorithm():
    n = 3
    simulator = Aer.get_backend('qasm_simulator')
    
    for oracle_func, expected in [(constant_oracle, 'constant'), (balanced_oracle, 'balanced')]:
        oracle = oracle_func(n, 0) if expected == 'constant' else oracle_func(n)
        qc = deutsch_jozsa_circuit(n, oracle)
        job = execute(qc, simulator, shots=1024)
        result = job.result()
        counts = result.get_counts()
        print(counts)

if __name__ == "__main__":
    test_algorithm()
