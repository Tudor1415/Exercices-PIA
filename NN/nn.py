import numpy as np

class Network:
    def __init__(self, architecture):
        self.layers = architecture["Layers"]
        self.activations = architecture["Activations"]
        self.w = self._init_weights()
        self.b = np.random.random((len(self.layers)))

    def _init_weights(self):
        weights = []
        for i in range(len(self.layers)-1):
            weights.append(np.random.random((self.layers[i+1], self.layers[i])))
            # print((self.layers[i+1], self.layers[i]))
        return weights

    def predict(self, input):
        output = input
        for i in range(len(self.layers)-1):
            output = self.w[i].dot(output)
            output = output + self.b[i]
            output = self.activations[i](output)
        return output

arch = {}
arch["Layers"] = [4,3,2,1]
arch["Activations"] = [lambda x: x+1 for i in range(4)]

nn = Network(arch)
pred = nn.predict(np.arange(4))
print(pred)

# Good resources:

# https://medium.com/@a.mirzaei69/implement-a-neural-network-from-scratch-with-python-numpy-backpropagation-e82b70caa9bb
# https://machinelearningmastery.com/implement-backpropagation-algorithm-scratch-python/