from ntm.neural.neuron import Neuron

print("===== NTM NEURON TEST =====")

neuron = Neuron(
    bias=0.1,
    activation="sigmoid"
)

inputs = [0.4, 0.18, -0.18]

result = neuron.forward(inputs)

print("Incoming signals:", inputs)
print("Bias:", neuron.bias)
print("Output:", result)

print("\n===== TEST COMPLETE =====")