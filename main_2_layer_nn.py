import time

import numpy as np

from util import cifar_10, nets

# pre-processing
start = time.time()
data, labels = cifar_10.unpickle("all")
data = data / 256
data -= np.mean(data)
print("--- Preparing time:\t{:4.2f}s".format(time.time() - start))

scale = (3072, 100, 10)
batch_size = 1000
step_size = 0.05
max_epoch = 10

nn = nets.TwoLayerNN(scale, batch_size, step_size, max_epoch, weights_init="Xavier")

# training
start = time.time()
for k in range(100):
    sample = np.random.randint(50000, size=batch_size)
    data_batch = data[sample]
    label_batch = labels[sample]
    nn.train(data_batch, label_batch, babysitter=True)  # turn babysitter True/False to view training process
print("--- Training time:\t{:4.2f}s".format((time.time() - start)))

# testing
if True:
    start = time.time()
    batch_test = cifar_10.unpickle("test_batch")
    data_test = batch_test[b'data'] / 256
    data_test -= np.mean(data_test)
    label_test = batch_test[b'labels']
    n_bingo = 0
    n_test = 10000

    for k in range(n_test):
        scores = nn.predict(data_test[k])
        if np.argmax(scores) == label_test[k]:
            n_bingo += 1

    print("--- Testing time:\t{:4.2f}s".format((time.time() - start)))
    print("--- Accuracy on test data: {}%".format(n_bingo * 100 / n_test))
