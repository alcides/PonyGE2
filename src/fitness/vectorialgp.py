from fitness.base_ff_classes.base_ff import base_ff
from sklearn.metrics import mean_squared_error
import numpy as np

# Load Dataset
dataset = [
    [1, 5, [1, 2, 3], [1, 5, 6], 0],
    [2, 2, [3, 2, 3], [1, 8, 6], 1],
    [1, 6, [2, 2, 3], [1, 5, 9], 2],
    [2, 8, [3, 2, 3], [1, 6, 6], 3],
]


class vectorialgp(base_ff):
    """
    VectorialGP is taken from:
    Azzali I, Vanneschi L, Silva S, Bakurov I, Giacobini M. A vectorial
    approach to genetic programming. In European Conference on Genetic
    Programming 2019 Apr 24 (pp. 213-227). Springer, Cham.
    """

    maximise = True  # True as it ever was.

    def __init__(self):
        # Initialise base fitness function class.
        super().__init__()

    def evaluate(self, ind, **kwargs):
        # ind.phenotype will be a string, including function definitions etc.
        # When we exec it, it will create a value XXX_output_XXX, but we exec
        # inside an empty dict for safety.

        def regressor(line):
            p, d = ind.phenotype, {"line": line, "np": np}
            # Exec the phenotype.
            exec(p, d)
            # Get the output
            return d["XXX_output_XXX"]  # this is the program's output: a number.

        y_pred = [regressor(line) for line in dataset]
        y = [line[-1] for line in dataset]
        r = mean_squared_error(y, y_pred)
        return r
