# -*- coding: utf-8 -*-
# Generated by codesnippet sphinx extension on 2020-11-22

import mdp
import numpy as np
np.random.seed(0)
import mdp
import bimdp
import dbn_binodes

n_layers = 2
flow = dbn_binodes.get_DBN_flow(2, hidden_dims=[2,2])

n_samples = 10000  # number of data points
n_greedy_reps = 100  # repetitions in greedy phase
x = mdp.numx.zeros((n_samples, 4))
for i in range(n_samples):
    r = mdp.numx.rand()
    if r>0.666:
        x[i,:] = [0.,1.,0.,1.]
    elif r>0.333:
        x[i,:] = [1.,0.,1.,0.]

data_iterables = [None] + [[x] * n_greedy_reps] * n_layers + [[x]]
msg_iterables = ([None] +
                 [[{"epsilon": 0.1, "decay": 0.0,
                    "momentum": 0.0}] * n_greedy_reps] * n_layers +
                 [[{"top_updates": 3, "epsilon": 0.1, "decay": 0.0,
                    "momentum": 0.0,
                    "max_iter": 2, "min_error": -1.0}]])

bimdp.show_training(flow, data_iterables, msg_iterables, debug=True)
# Expected:
## '/tmp/.../training_inspection.html'
print "done."
# Expected:
## done.
