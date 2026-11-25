#training data
inputs = [1,2,3,4,5]
outputs = [2,4,6,8,10]

#initial parameter
weights = 0.5
bias = 0
learning_rate = 0.35

#prediction
def predict(x):
    return x * weights + bias

#error calc
# prediction = predict(3)
# correct_ans = 6
# error = prediction - correct_ans
# print(error)

# avg squared error
def calculate_loss():
    total_error = 0
    for x, y in zip(inputs, outputs):
        prediction = predict(x)
        error = prediction - y
        total_error += error ** 2
    return total_error / len(inputs)

# print(calculate_loss()) 

#training
for epoch in range(2000):
    weight_gradient = 0
    bias_gradient = 0

    for x, y in zip(inputs, outputs):
            prediction = predict(x)
            error = prediction - y

            weight_gradient += 2 * x * error
            bias_gradient += 2 * error

            weight_gradient /= len(inputs)
            bias_gradient /= len(inputs)

            weights -= learning_rate * weight_gradient
            bias -= learning_rate * bias_gradient


            #progress
            if epoch % 100 == 0:
                 print(
                      "epoch", epoch,
                      "loss", calculate_loss()
                 )

#trained network
print("\nFinal weight:", weights)
print("Final bias:", bias)

print("\nPredictions:")

for x in inputs:
    print(x, "->", predict(x))

print("-------------------CUSTOM INPUTS----------------------")

value = int(input("Enter value: "))
print(predict(value))