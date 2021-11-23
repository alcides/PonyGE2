#! /usr/bin/env python

# PonyGE2
# Copyright (c) 2017 Michael Fenton, James McDermott,
#                    David Fagan, Stefan Forstenlechner,
#                    and Erik Hemberg
# Hereby licensed under the GNU GPL v3.
""" Python GE implementation """
from time import perf_counter_ns

from utilities.algorithm.general import check_python_version

check_python_version()

from stats.stats import get_stats
from algorithm.parameters import params, set_params
import sys

def preprocess():
    set_params(sys.argv[1:])

def evolve():
    return params['SEARCH_LOOP']()

def mane():
    """ Run program """
    processing_time = perf_counter_ns()
    algorithm = preprocess()
    processing_time = perf_counter_ns() - processing_time

    # Check the evolution time
    evolution_time = perf_counter_ns()
    individuals = evolve()
    evolution_time = perf_counter_ns() - evolution_time
    
    # Print final review
    # get_stats(individuals, end=True)

    f = open(f"results/ponyge/temp_times.csv", "a")
    f.write(f"\n{processing_time},{evolution_time}")
    f.close()


if __name__ == "__main__":
    mane()
