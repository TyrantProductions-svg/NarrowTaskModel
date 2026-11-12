
from ntm.neural.neuron import Neuron
from ntm.neural.synapse import Synapse
from ntm.neural.network import Network


print("===== NTM NETWORK TEST =====")

# Create input neurons
input_a = Neuron(activation="relu")
input_b = Neuron(activation="relu")

# Create processing neurons
hidden = Neuron(bias=0.1, activation="sigmoid")
output = Neuron(bias=-0.1, activation="sigmoid")

# Create synapses
synapse_a = Synapse(input_a, hidden, weight=0.5)
synapse_b = Synapse(input_b, hidden, weight=-0.25)

synapse_c = Synapse(hidden, output, weight=0.7)

# Assemble the network
network = Network(
    input_neurons=[input_a, input_b],
    neurons=[hidden, output],
    synapses=[synapse_a, synapse_b, synapse_c],
    output_neurons=[output]
)

# Run the network
inputs = [0.8, 0.4]

results = network.forward(inputs)

print("External inputs:", inputs)
print("Hidden neuron output:", hidden.output)
print("Final output:", results)

print("\n===== TEST COMPLETE =====")
