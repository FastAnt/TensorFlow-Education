import tensorflow as tf

x_ = tf.placeholder(tf.float, shape = [100,4]   , name="x-input")
y_ = tf.placeholder(tf.int8,  shape = [100,700] , name="y-output")
