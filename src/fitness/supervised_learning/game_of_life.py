import numpy as np
from algorithm.parameters import params
from fitness.base_ff_classes import base_ff
from fitness.supervised_learning.supervised_learning import supervised_learning
from sklearn.metrics import accuracy_score as sklearn_accuracy
from sklearn.metrics import f1_score as sklearn_f1
from utilities.fitness.get_data import get_data
from utilities.fitness.error_metric import f1_score

class game_of_life(supervised_learning):
    """Fitness function for game_of_life classifier.

    The candidate solutions are like this:
    
    (x[:, 0, 1] | ((x[:, 0, -1] | ((x[:, -1, -1] & x[:, 1, 1])))))  

    The possible outputs are 0 and 1. The inputs (3, 3) are composed
    of 0 and 1s. The variables x[i] are from -1 to 1.

    An example command-line is then:
    
    python ponyge.py --parameters ../parameters/game_of_life
    
    or setting the parameters manually:

    python ponyge.py --fitness supervised_learning.game_of_life \
    --grammar supervised_learning/game_of_life.bnf \ 
    --dataset_train ../datasets/GameOfLife/Train.csv \
    --dataset_test ../datasets/GameOfLife/Test.csv \
    --dataset_delimiter ,
    """
    def __init__(self):
        # Initialise base fitness function class.
        super().__init__()

        # Convert 2d dataset into 3d, where each instance
        # is a 3x3 matrix
        self.training_in = self.training_in.reshape(self.training_in.shape[0], 3, 3)
        self.test_in = self.test_in.reshape(self.test_in.shape[0], 3, 3)

        self.training_in = self.training_in.astype(int)
        self.test_in = self.test_in.astype(int)
        
        if params['ERROR_METRIC'] is None:
            params['ERROR_METRIC'] = f1_score

        self.maximise = params['ERROR_METRIC'].maximise
