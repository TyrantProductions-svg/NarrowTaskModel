
class Synapse:

    def __init__(self, source, target, weight=0.5):

        self.source = source
        self.target = target
        self.weight = weight

    def transmit(self):

        signal = self.source.output * self.weight

        return signal

    def update_weight(self, adjustment):

        self.weight += adjustment
