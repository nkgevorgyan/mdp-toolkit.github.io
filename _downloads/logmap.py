# -*- coding: utf-8 -*-
# Generated by codesnippet sphinx extension on 2020-11-22

import mdp
import numpy as np
np.random.seed(0)
p2 = np.pi*2
t = np.linspace(0, 1, 10000, endpoint=0) # time axis 1s, samplerate 10KHz
dforce = np.sin(p2*5*t) + np.sin(p2*11*t) + np.sin(p2*13*t)
def logistic_map(x, r):
    return r*x*(1-x)

series = np.zeros((10000, 1), 'd')

series[0] = 0.6

for i in range(1,10000):
    series[i] = logistic_map(series[i-1],3.6+0.13*dforce[i])

flow = (mdp.nodes.EtaComputerNode() +
        mdp.nodes.TimeFramesNode(10) +
        mdp.nodes.PolynomialExpansionNode(3) +
        mdp.nodes.SFANode(output_dim=1) +
        mdp.nodes.EtaComputerNode() )

flow.train(series)

slow = flow(series)

resc_dforce = (dforce - np.mean(dforce, 0)) / np.std(dforce, 0)

print '%.3f' % mdp.utils.cov2(resc_dforce[:-9], slow)
# Expected:
## 1.000

print 'Eta value (time series): %d' % flow[0].get_eta(t=10000)
# Expected:
## Eta value (time series): 3004
print 'Eta value (slow feature): %.3f' % flow[-1].get_eta(t=9996)
# Expected:
## Eta value (slow feature): 10.218
