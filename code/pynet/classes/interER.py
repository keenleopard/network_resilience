from __future__ import division, print_function

import networkx as nx
import numpy as np
from .interGraph import InterGraph

class InterER(InterGraph):

    def __init__(self):
        """
        initialize interdependent ER networks.
        """
