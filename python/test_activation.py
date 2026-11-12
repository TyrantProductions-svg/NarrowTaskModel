
from ntm.neural.activation import sigmoid, relu, tanh


print("===== NTM ACTIVATION TEST =====")

# Test sigmoid
print("\nTesting Sigmoid:")
print("Input: 0")
print("Output:", sigmoid(0))

# Test ReLU
print("\nTesting ReLU:")
print("Input: -5")
print("Output:", relu(-5))

print("Input: 5")
print("Output:", relu(5))

# Test tanh
print("\nTesting Tanh:")
print("Input: 1")
print("Output:", tanh(1))

print("\n===== TEST COMPLETE =====")
