#! /usr/bin/env python

# PonyGE2
# Copyright (c) 2017 Michael Fenton, James McDermott,
#                    David Fagan, Stefan Forstenlechner,
#                    and Erik Hemberg
# Hereby licensed under the GNU GPL v3.
""" Python GE implementation """

from utilities.algorithm.general import check_python_version

check_python_version()

from stats.stats import get_stats
from algorithm.parameters import params, set_params
import sys
import copy

default_params = copy.deepcopy(params)

def preprocess(parameters):
    set_params(parameters)

def evolve():
    return params['SEARCH_LOOP']()
    
def reset_ponyge():
    params = default_params

def mane():
    """ Run program """
    preprocess(sys.argv[1:])   # exclude the ponyge.py arg itself

    # Run evolution
    individuals = evolve()
    
    # Print final review
    get_stats(individuals, end=True)


if __name__ == "__main__":
    mane()
