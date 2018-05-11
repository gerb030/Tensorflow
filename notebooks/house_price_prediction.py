# example code
import tensorflow as tf 
import numpy as np
import math 
import matplotlib
import matplotlib.pyplot as plt 
import matplotlib.animation as animation # animation support


# generation
num_house = 160
np.random.seed(743)
house_size = np.random.randint(low=1000, high=3500, size=num_house)

# generation with random noise 
np.random.seed(142)
house_price = house_size * 100.0 + np.random.randint(low=20000, high=70000, size=num_house)

# plot data
plt.plot(house_size, house_price, "bx") #bx = blue X
plt.ylabel("Price")
plt.xlabel("Size")
plt.show()

# normalize values to prevent under/overflows
def normalize(array):
    return (array - array.mean()) / array.std()

# define number of training samples
num_train_samples = math.floor(num_house * 0.7)

# define training data
train_house_size = np.asarray(house_size[:num_train_samples])
train_price = np.asanyarray(house_price[:num_train_samples:])

train_house_size_norm = normalize(train_price)
train_price_norm = normalize(train_price)

# define test data
test_house_size = np.array(house_size[num_train_samples:])
test_house_price = np.array(house_price[num_train_samples:])

test_house_size_norm = normalize(test_house_size)
test_house_price_norm = normalize(test_house_price)
  
tf_house_price = tf.placeholder("float", name="house_size")
tf_price = tf.placeholder("float", name="price")



