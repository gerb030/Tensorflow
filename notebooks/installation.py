# import TensorFlow
import tensorflow as tf 

sess = tf.Session()

#verify we can print
hello = tf.constant("Hello world")
print(sess.run(hello))

a = tf.constant(20)
b = tf.constant(22)
print('a + b = {0}'.format(sess.run(a + b)))
