from __future__ import division, print_function

from .inter_er import InterER

class Simulation(object):
    """
    Simulation class for cascading failure of interdependent network.
    """

    def __init__(
            self,
            n=1000,
            k=4,
            working_fraction=1.,
            remove_subnet='a',
            remove_type="fail"
        ):
        """
        n: No. nodes of each sub network
        k: average degree
        1 - working fraction: fraction of removed nodes
        remove_subnet: 'a' or 'b'
        remove_type: 'fail' or 'attack'
        """

        self.n = n
        self.k = k
        self.G = InterER(n,k,k)
        self.G.one2one()
        if remove_type == "fail" or "f":
            G.fail(subnet=remove_subnet, Q=(1-working_fraction)*n)



    @property
    def frac_gmcc(self):
        """
        fraction of No. nodes in the Giant Mutually Connected Component (GMCC).
        """



