from __future__ import division, print_function

import networkx as nx
import numpy as np
from .interGraph import InterGraph

class InterSF(InterGraph):

    def __init__(self):
        """
        initialize interdependent Scale-Free (SF) networks.
        """

