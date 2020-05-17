# -*- coding: utf-8 -*-
# Generated by codesnippet sphinx extension on 2020-05-17

import mdp
import numpy as np
np.random.seed(0)
node1 = mdp.nodes.PCANode(input_dim=100, output_dim=10)
node2 = mdp.nodes.SFA2Node(input_dim=10, output_dim=10)
parallel_flow = mdp.parallel.ParallelFlow([node1, node2])
parallel_flow2 = parallel_flow.copy()
parallel_flow3 = parallel_flow.copy()
n_data_chunks = 10
data_iterables = [[np.random.random((50, 100))
                   for _ in range(n_data_chunks)]] * 2
scheduler = mdp.parallel.ProcessScheduler()
parallel_flow.train(data_iterables, scheduler=scheduler)
scheduler.shutdown()

scheduler = mdp.parallel.ProcessScheduler()
try:
    parallel_flow2.train(data_iterables, scheduler=scheduler)
finally:
    scheduler.shutdown()

with mdp.parallel.ProcessScheduler() as scheduler:
    parallel_flow3.train(data_iterables, scheduler=scheduler)
