
from ntm.neural.neuron import Neuron
from ntm.neural.synapse import Synapse


print("===== NTM SYNAPSE TEST =====")

# Create two neurons
neuron_a = Neuron([1.0], bias=0.0, activation="relu")
neuron_b = Neuron([1.0], bias=0.0, activation="relu")

# Give neuron A an input
neuron_a.forward([0.8])

# Connect the neurons
connection = Synapse(neuron_a, neuron_b, weight=0.5)

# Transmit the signal
signal = connection.transmit()

print("Source output:", neuron_a.output)
print("Connection weight:", connection.weight)
print("Transmitted signal:", signal)

# Modify the connection weight
connection.update_weight(0.2)

print("Updated weight:", connection.weight)

print("\n===== TEST COMPLETE =====")
