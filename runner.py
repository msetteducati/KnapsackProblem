import argparse
import time
from knapsackproblem import *

"""
This file is for running specified knapsack problem algorithms on certain problem sizes
as specified by the assignment document. The algorithm to run is specified by the optional
command line arguments.
"""


# create argument list for command line input
parser = argparse.ArgumentParser()
parser.add_argument("n_min", type=int, help="minimum number of items to run the algorithm(s) on")
parser.add_argument("n_max", type=int, help="maximum number of items to run the algorithm(s) on")
parser.add_argument("n_step", type=int, help="step size for number of items for subsequent runs of the algorithm(s)")
parser.add_argument("--bruteforce", help="run brute force algorithm for n=1, 2, 3, ..., 30", action="store_true")
parser.add_argument("--greedy", help="run greedy algorithm for n=100k, 200k, 300k, ..., 3M", action="store_true")
parser.add_argument("--dynamic", help="run dynamic programming algorithm for n=25, 50, 75, ..., 750", action="store_true")
parser.add_argument("--log", help="use this flag for logging output throughout algorithms", action="store_true")
args = parser.parse_args()


# run algorithms as per arguments
if args.bruteforce:
    print("Brute Force Algorithm Runs:")
    print("n\ttime (s)")
    for i in range(args.n_min, args.n_max + args.n_step, args.n_step):
        if args.log:
            my_problem = generate_random_knapsack_problem(i, log=True)
        else:
            my_problem = generate_random_knapsack_problem(i)

        # track time, run algorithm, print n and time
        start = time.time()
        brute_force_sln = my_problem.brute_force_solution()
        end = time.time()

        print(i, "\t", (end-start))

if args.greedy:
    print("Greedy Algorithm Runs:")
    print("n\ttime (s)")
    for i in range(args.n_min, args.n_max + args.n_step, args.n_step):
        if args.log:
            my_problem = generate_random_knapsack_problem(i, log=True)
        else:
            my_problem = generate_random_knapsack_problem(i)

        start = time.time()
        greedy_sln = my_problem.greedy_solution()
        end = time.time()

        print(i, "\t", (end-start))

if args.dynamic:
    print("Dynamic Programming Algorithm Runs:")
    print("n\ttime (s)\t\toptimality")
    for i in range(args.n_min, args.n_max + args.n_step, args.n_step):
        if args.log:
            my_problem = generate_random_knapsack_problem(i, log=True)
        else:
            my_problem = generate_random_knapsack_problem(i)

        start = time.time()
        dynamic_sln = my_problem.dynamic_solution()
        end = time.time()

        greedy_sln = my_problem.greedy_solution()
        if dynamic_sln != 0:
            optimality = greedy_sln/dynamic_sln
        else:
            optimality = None

        print(i, "\t", (end-start), "\t", optimality)
