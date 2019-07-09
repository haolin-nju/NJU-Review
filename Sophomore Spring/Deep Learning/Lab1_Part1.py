### 1.1
import tensorflow as tf
tf.enable_eager_execution()
import numpy as np
import matplotlib.pyplot as plt

# Create the nodes in the graph, and initialize values
a = tf.constant(15, name="a")
b = tf.constant(61, name="b")

# Add them!
c = tf.add(a,b, name="c")
print(c)

# Construct a simple computation graph
def graph(a,b):
  #TODO: Define the operation for c, d, e (use tf.add, tf.subtract, tf.multiply).
  c = tf.add(a,b,name="c")# TODO
  d = tf.subtract(b,1,name="d")# TODO
  e = tf.multiply(c,d,name="e")# TODO
  return e

# Consider example values for a,b
a, b = 1.5, 2.5
# Execute the computation
e_out = graph(a,b)
print(e_out)

### 1.2
# n_in: number of inputs
# n_out: number of outputs
def our_dense_layer(x, n_in, n_out):
  # Define and initialize parameters, a weight matrix W and biases b
  W = tf.Variable(tf.ones((n_in, n_out)))
  b = tf.Variable(tf.zeros((1, n_out)))
  
  #TODO: define the operation for z (hint: use tf.matmul)
  z = tf.matmul(x,W,name="z")+b# TODO
  
  #TODO: define the operation for out (hint: use tf.sigmoid)
  out = tf.sigmoid(z)# TODO
  return out

#TODO: define an example input x_input
x_input = tf.constant([[1.,2.]])# TODO
#TODO: call `our_dense_layer` to get the output of the network and print the result!
print(our_dense_layer(x_input,n_in=2,n_out=1)) # TODO

# Import relevant packages
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

# Define the number of inputs and outputs
n_input_nodes = 2
n_output_nodes = 3

# First define the model 
model = Sequential()

#TODO: Define a dense (fully connected) layer to compute z
# Remember: dense layers are defined by the parameters W and b!
# You can read more about the initialization of W and b in the TF documentation :) 
dense_layer = Dense(n_output_nodes,input_shape=(n_input_nodes,),activation='sigmoid')# TODO

# Add the dense layer to the model
model.add(dense_layer)

# Test model with example input
x_input = tf.constant([[1,2.]], shape=(1,2))

#TODO: feed input into the model and predict the output!
print(model(x_input)) # TODO

### 1.3
x = tf.Variable([tf.random.normal([1])])
print("Initializing x={}".format(x.numpy()))
learning_rate = 1e-2
history = []

for i in range(500):
  with tf.GradientTape() as tape:
    y = (x - 1)**2 # record the forward pass on the tape

  grad = tape.gradient(y, x) # compute the gradient of y with respect to x
  new_x = x - learning_rate*grad # sgd update
  x.assign(new_x) # update the value of x
  history.append(x.numpy()[0])

plt.plot(history)
plt.plot([0, 500],[1,1])
plt.legend(('Predicted', 'True'))
plt.xlabel('Iteration')
plt.ylabel('x value')
plt.show()

### 1.4
a = tf.constant(12)
counter = 0
while not tf.equal(a, 1):
  if tf.equal(a % 2, 0):
    a = a / 2
  else:
    a = 3 * a + 1
  print(a)
