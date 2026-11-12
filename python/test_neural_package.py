
from ntm.neural import (
    Neuron,
    Synapse,
    Network,
    hebbian_learning,
    sigmoid,
    relu,
    tanh
)

print("===== NTM NEURAL PACKAGE TEST =====")

print("Neuron:", Neuron)
print("Synapse:", Synapse)
print("Network:", Network)
print("Hebbian learning:", hebbian_learning)

print("Sigmoid(0):", sigmoid(0))
print("ReLU(-5):", relu(-5))
print("Tanh(1):", tanh(1))

print("\n===== TEST COMPLETE =====")
