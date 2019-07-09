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
