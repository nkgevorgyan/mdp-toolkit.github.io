# -*- coding: utf-8 -*-
# Generated by codesnippet sphinx extension on 2020-05-17

import mdp
import numpy as np
np.random.seed(0)
import mdp
import numpy
import os
import matplotlib
matplotlib.rcParams['examples.directory'] = os.path.join(os.path.dirname(matplotlib.rcParams['datapath']), 'sample_data')
import pylab
from matplotlib.cbook import get_sample_data
im = pylab.imread(get_sample_data("ada.png"))
im = numpy.sqrt((im[:,:,:3]**2.).mean(2))

pi = numpy.pi
orientations = [0., pi/4., pi/2., pi*3./4.]
freq = 1./10    # frequency
phi = pi/2.     # phase
size = (20, 20) # in pixels
sgm = (5., 3.)  # standard deviation of the axes
nfilters = len(orientations)
gabors = numpy.empty((nfilters, size[0], size[1]))
for i, alpha in enumerate(orientations):
    gabors[i,:,:] = mdp.utils.gabor(size, alpha, phi, freq, sgm)

node = mdp.nodes.Convolution2DNode(gabors, mode='valid', boundary='fill',
                                   fillvalue=0, output_2d=False)
cim = node.execute(im[numpy.newaxis,:,:])

x = mdp.utils.lrep(im, 3)
from timeit import Timer
timer = Timer("node.execute(x)", "from __main__ import node, x")
print timer.repeat(1, 1), 'sec'
# Expected:
## 6.91 sec
with mdp.caching.cache(cache_classes=[mdp.nodes.Convolution2DNode]):
   print timer.repeat(1, 1), 'sec'
   print timer.repeat(1, 1), 'sec'
# Expected:
## 7.05 sec
## 39.6 msec
