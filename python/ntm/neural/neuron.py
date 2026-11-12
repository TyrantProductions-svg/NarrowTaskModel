
from ntm.neural.activation import sigmoid, relu, tanh


class Neuron:

    def __init__(self, bias=0.0, activation="sigmoid"):
        self.bias = bias
        self.activation = activation

        self.output = 0.0

    def activate(self, value):

        if self.activation == "sigmoid":
            return sigmoid(value)

        elif self.activation == "relu":
            return relu(value)

        elif self.activation == "tanh":
            return tanh(value)

        else:
            raise ValueError("Unknown activation function")

    def forward(self, inputs):

        weighted_sum = sum(inputs)

        weighted_sum += self.bias

        self.output = self.activate(weighted_sum)

        return self.output
