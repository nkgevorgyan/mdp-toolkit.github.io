# -*- coding: utf-8 -*-
# Generated by codesnippet sphinx extension on 2020-11-06

import mdp
import numpy as np
np.random.seed(0)
class BogusNode(mdp.Node):
    """This node does nothing."""
    def _train(self, x):
        pass
class BogusNode2(mdp.Node):
    """This node does nothing. But it's neither trainable nor invertible.
    """
    def is_trainable(self): return False
    def is_invertible(self): return False

def gen_data(blocks):
    for i in mdp.utils.progressinfo(xrange(blocks)):
        block_x = np.atleast_2d(np.arange(2.,1001,2))
        block_y = np.atleast_2d(np.arange(1.,1001,2))
        # put variables on columns and observations on rows
        block = np.transpose(np.concatenate([block_x,block_y]))
        yield block

flow = mdp.Flow([BogusNode(),BogusNode()], verbose=1)

flow.train([gen_data(5000),gen_data(3000)])
# Expected:
## Training node #0 (BogusNode)
## <BLANKLINE>
## [===================================100%==================================>]
## <BLANKLINE>
## Training finished
## Training node #1 (BogusNode)
## [===================================100%==================================>]
## <BLANKLINE>
## Training finished
## Close the training phase of the last node

flow = BogusNode() + BogusNode()
block_x = np.atleast_2d(np.arange(2.,1001,2))
block_y = np.atleast_2d(np.arange(1.,1001,2))
single_block = np.transpose(np.concatenate([block_x,block_y]))
flow.train(single_block)

flow = mdp.Flow([BogusNode2(),BogusNode()], verbose=1)
flow.train([None, gen_data(5000)])
# Expected:
## Training node #0 (BogusNode2)
## Training finished
## Training node #1 (BogusNode)
## [===================================100%==================================>]
## <BLANKLINE>
## Training finished
## Close the training phase of the last node

flow = mdp.Flow([BogusNode2(),BogusNode()], verbose=1)
flow.train(single_block)
# Expected:
## Training node #0 (BogusNode2)
## Training finished
## Training node #1 (BogusNode)
## Training finished
## Close the training phase of the last node

flow = mdp.Flow([BogusNode(),BogusNode()], verbose=1)
flow.train([gen_data(1), gen_data(1)])
# Expected:
## Training node #0 (BogusNode)
## Training finished
## Training node #1 (BosgusNode)
## [===================================100%==================================>]
## <BLANKLINE>
## Training finished
## Close the training phase of the last node
output = flow.execute(gen_data(1000))
# Expected:
## [===================================100%==================================>]
output = flow.inverse(gen_data(1000))
# Expected:
## [===================================100%==================================>]

output = flow(single_block)
output = flow.inverse(single_block)

class SimpleIterable(object):
    def __init__(self, blocks):
        self.blocks = blocks
    def __iter__(self):
        # this is a generator
        for i in range(self.blocks):
            yield generate_some_data()

class RandomIterable(object):
    def __init__(self):
        self.state = None
    def __iter__(self):
        if self.state is None:
            self.state = np.random.get_state()
        else:
            np.random.set_state(self.state)
        for i in range(2):
            yield np.random.random((1,4))
iterable = RandomIterable()
for x in iterable:
    print x
# Expected:
## [[ 0.5488135   0.71518937  0.60276338  0.54488318]]
## [[ 0.4236548   0.64589411  0.43758721  0.891773  ]]
for x in iterable:
    print x
# Expected:
## [[ 0.5488135   0.71518937  0.60276338  0.54488318]]
## [[ 0.4236548   0.64589411  0.43758721  0.891773  ]]
