# -*- coding: utf-8 -*-
# Generated by codesnippet sphinx extension on 2020-05-17

import mdp
import numpy as np
np.random.seed(0)
def s_distr(npoints, hole=False):
    """Return a 3D S-shaped surface. If hole is True, the surface has
    a hole in the middle."""
    t = mdp.numx_rand.random(npoints)
    y = mdp.numx_rand.random(npoints)*5.
    theta = 3.*mdp.numx.pi*(t-0.5)
    x = mdp.numx.sin(theta)
    z = mdp.numx.sign(theta)*(mdp.numx.cos(theta) - 1.)
    if hole:
        indices = mdp.numx.where(((0.3>t) | (0.7<t)) | ((1.>y) | (4.<y)))
        return x[indices], y[indices], z[indices], t[indices]
    else:
        return x, y, z, t

n, k = 1000, 15
x, y, z, t = s_distr(n, hole=False)
data = mdp.numx.array([x,y,z]).T
lle_projected_data = mdp.nodes.LLENode(k, output_dim=2)(data)

x, y, z, t = s_distr(n, hole=True)
data = mdp.numx.array([x,y,z]).T
lle_projected_data = mdp.nodes.LLENode(k, output_dim=2)(data)

hlle_projected_data = mdp.nodes.HLLENode(k, output_dim=2)(data)
