import argparse
from knapsackproblem import *

"""
This file is for running specified knapsack problem algorithms given some input n.
This runner file was used for testing the program, and does not output the required
information as per the project. runner.py should be used for running the instances of 
the problem as specified by the assignment.
"""


# create argument list for command line input
parser = argparse.ArgumentParser()
parser.add_argument("n", type=int, help="total number of items for the thief to choose from")
parser.add_argument("--bruteforce", help="run brute force algorithm", action="store_true")
parser.add_argument("--greedy", help="run greedy algorithm", action="store_true")
parser.add_argument("--dynamic", help="run dynamic programming algorithm", action="store_true")
parser.add_argument("--log", help="use this flag for logging output throughout algorithms", action="store_true")
args = parser.parse_args()

if args.log:
    my_problem = generate_random_knapsack_problem(args.n, log=True)
else:
    my_problem = generate_random_knapsack_problem(args.n)

# run algorithms as per arguments
if args.bruteforce:
    brute_force_sln = my_problem.brute_force_solution()

if args.greedy:
    greedy_sln = my_problem.greedy_solution()

if args.dynamic:
    dynamic_sln = my_problem.dynamic_solution()
