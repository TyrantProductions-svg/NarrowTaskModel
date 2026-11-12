
from ntm.neural.neuron import Neuron
from ntm.neural.synapse import Synapse
from ntm.neural.learning_rules import hebbian_learning


print("===== NTM LEARNING RULE TEST =====")

# Create two neurons
neuron_a = Neuron(activation="relu")
neuron_b = Neuron(activation="relu")

# Give them activity
neuron_a.forward([0.8])
neuron_b.forward([0.6])

# Connect them
connection = Synapse(
    neuron_a,
    neuron_b,
    weight=0.5
)

print("Initial weight:", connection.weight)

# Apply Hebbian learning
adjustment = hebbian_learning(
    connection,
    learning_rate=0.1
)

print("Weight adjustment:", adjustment)
print("Updated weight:", connection.weight)

print("\n===== TEST COMPLETE =====")
