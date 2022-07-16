import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot

# create a class for randomwalk
class RandomWalk:

    def __init__(self):
        """
        Generate RandomWalk plot
        """
        walk = [99]

        for i in range(1900):
            # Create random noise
            noise = -1 if np.random.random() < 0.5 else 1
            walk.append(walk[-1] + noise)

        plt.savefig("../output/"+"randomWalk.png")

        autocorrelation_plot(walk)
        plt.savefig("../output/randomWalkAutocorrelation.png")
        self.walk = walk
