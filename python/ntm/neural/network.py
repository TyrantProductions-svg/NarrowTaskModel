
class Network:

    def __init__(self, input_neurons, neurons, synapses, output_neurons):

        self.input_neurons = input_neurons
        self.neurons = neurons
        self.synapses = synapses
        self.output_neurons = output_neurons

    def forward(self, inputs):

        if len(inputs) != len(self.input_neurons):
            raise ValueError("Input count must match input neuron count")

        # Assign external inputs to input neurons
        for neuron, value in zip(self.input_neurons, inputs):
            neuron.output = value

        # Process neurons in order
        for neuron in self.neurons:

            incoming_signals = []

            # Collect signals from connected synapses
            for synapse in self.synapses:

                if synapse.target is neuron:
                    incoming_signals.append(synapse.transmit())

            # Activate the receiving neuron
            neuron.forward(incoming_signals)

        # Collect final outputs
        outputs = []

        for neuron in self.output_neurons:
            outputs.append(neuron.output)

        return outputs
