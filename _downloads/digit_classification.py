# -*- coding: utf-8 -*-
# Generated by codesnippet sphinx extension on 2020-11-22

import mdp
import numpy as np
np.random.seed(0)
import mdp
import numpy
import sklearn as sl
from sklearn import datasets
digits = datasets.load_digits()
images = digits.images.astype('f')
labels = digits.target
data = digits.images.reshape((images.shape[0],
                              numpy.prod(images.shape[1:])))

ntrain = images.shape[0] // 3 * 2
train_data = [data[:ntrain, :]]
train_data_with_labels = [(data[:ntrain, :], labels[:ntrain])]
test_data = data[ntrain:, :]
test_labels = labels[ntrain:]

flow = mdp.Flow([mdp.nodes.PCANode(output_dim=25, dtype='f'),
                 mdp.nodes.PolynomialExpansionNode(3),
                 mdp.nodes.PCANode(output_dim=0.99),
                 mdp.nodes.FDANode(output_dim=9),
                 mdp.nodes.SVCScikitsLearnNode(kernel='rbf')], verbose=True)

flow.train([train_data, None, train_data,
            train_data_with_labels, train_data_with_labels])
# Expected:
## Training node #0 (PCANode)
## Training finished
## Training node #1 (PolynomialExpansionNode)
## Training finished
## Training node #2 (PCANode)
## Training finished
## Training node #3 (FDANode)
## Training finished
## Training node #4 (SVCScikitsLearnNode)
## Training finished
## Close the training phase of the last node
print repr(flow)
# Expected:
## Flow([PCANode(input_dim=64, output_dim=25, dtype='float32'),
##       PolynomialExpansionNode(input_dim=25, output_dim=3275, dtype='float32'),
##       PCANode(input_dim=3275, output_dim=646, dtype='float32'),
##       FDANode(input_dim=646, output_dim=9, dtype='float32'),
##       SVCScikitsLearnNode(input_dim=9, output_dim=9, dtype='float32')])

flow[-1].execute = flow[-1].label
prediction = flow(test_data)
error = ((prediction.flatten() != test_labels).astype('f').sum()
         / (images.shape[0] - ntrain) * 100.)
print 'percent error:', error
# Expected:
## percent error: 3.33889816361
