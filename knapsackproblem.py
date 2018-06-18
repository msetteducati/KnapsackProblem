import random


def generate_random_knapsack_problem(n, log=False):
    """
    Creates a random instance of KnapsackProblem where there are n items.
    :param n: The total number of items available to add to the knapsack
    :param log: Whether or not to log details of the program throughout instantiation and the algorithms
    :return: A new instance of a KnapsackProblem object
    """
    def generate_random_items():
        to_return = []

        for x in range(n):
            random_weight = random.randint(1, n)
            random_value = random.randint(1, n)
            to_return.append(Item(random_weight, random_value))

        return to_return

    def compute_weight_capacity(items):
        sum_weights = sum([item.weight for item in items])
        return int(sum_weights * 0.75)

    my_items = generate_random_items()
    my_weight_capacity = compute_weight_capacity(my_items)

    return KnapsackProblem(n, my_items, my_weight_capacity, log=log)


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __str__(self):
        return "{'weight': " + str(self.weight) + \
               ", 'value': " + str(self.value) + "}"


class KnapsackProblem:
    def __init__(self, n, items, weight_capacity, log=False):
        self.n = n
        self.items = items
        self.weight_capacity = weight_capacity
        self.log = log

        if self.log:
            print("Knapsack Problem Instance Variables")
            print(" n: ", self.n)
            print(" weight capacity: ", self.weight_capacity)
            print(" items:")
            for item in self.items:
                print(" \t", item)
            print("")

    def brute_force_solution(self):
        """
        Wrapper function for recursive brute force algorithm
        :return: optimal value of haul
        """

        def solve_by_brute_force(cur_i, available_weight):
            """
            Recursive function returns that returns the value of the items taken to this index
            :param cur_i: index that we are checking
            :param available_weight: available weight for more items
            :return: value of items taken to this point
            """
            # base case: we have looked at every element or cur_weight is at capacity
            if cur_i == -1 or available_weight == 0:
                return 0

            # if item doesn't fit, leave it
            if self.items[cur_i].weight > available_weight:
                return solve_by_brute_force(cur_i - 1, available_weight)  # leave item

            # solve in both cases: take item and leave item
            take = self.items[cur_i].value + solve_by_brute_force(cur_i - 1, available_weight - self.items[cur_i].weight)
            leave = solve_by_brute_force(cur_i - 1, available_weight)

            # take the max of leaving or taking item
            return max(take, leave)

        optimal_value = solve_by_brute_force(self.n - 1, self.weight_capacity)

        if self.log:
            print("Brute Force Solution\n", "Optimal Value: ", optimal_value, "\n")

        return optimal_value

    def greedy_solution(self):
        """
        Function for solving knapsack problem using a greedy approach. The algorithm takes the most value-dense items
        until the knapsack is full.
        :return: The value of the haul
        """
        # Create local class for items with density
        class ItemWithDensity(Item):
            def __init__(self, weight, value):
                super().__init__(weight, value)
                self.density = self.value/self.weight

            def __str__(self):
                return "{'weight': " + str(self.weight) + \
                       ", 'value': " + str(self.value) + \
                       ", 'density': " + str(self.density) + "}"

        # create new array with items with density and sort by density
        items_with_density = [ItemWithDensity(item.weight, item.value) for item in self.items]
        items_with_density.sort(key=lambda item: item.density, reverse=True)

        if self.log:
            print("Greedy Solution\n", "Items sorted by density: ")

        # add value of items if there is weight available starting with most dense (previously sorted)
        available_weight = self.weight_capacity
        total_value = 0
        for item in items_with_density:
            if item.weight <= available_weight:
                total_value += item.value
                available_weight -= item.weight

            if self.log:
                print("\t", item)

        if self.log:
            print(" Total value: ", total_value)
            print("")

        return total_value

    def dynamic_solution(self):
        """
        Function for solving knapsack problem using a dynamic programming approach. The algorithm creates a 2D array
        and tracks every scenario for available weight and items taken, and fills in the array in a bottom-up
        fashion. The value at the 'bottom-right' corner of the array is the optimal value.
        :return: The value of the haul (optimal value)
        """
        if self.log:
            print("Dynamic Programming Solution")
            print(" Computed Solutions Array: ")

        # array for storing already computer solutions; rows are weights, columns are indices
        # ex: computed_slns[weight][i]
        computed_slns = [[None] * (self.n + 1) for row in range(self.weight_capacity + 1)]

        for row in range(self.weight_capacity + 1):
            for col in range(self.n + 1):
                # if the weight available or items available is 0, the solution is 0
                if row == 0 or col == 0:
                    computed_slns[row][col] = 0

                # if the weight of this item is less than or equal to the weight available
                elif self.items[col-1].weight <= row:
                    # get values for this item
                    my_weight = self.items[col-1].weight
                    my_value = self.items[col-1].value

                    # get the max of whether this item is left or taken
                    # if item is taken, add the value and get the solution from the remaining weight
                    # if item is left, the solution is the same as previous item
                    computed_slns[row][col] = max(my_value + computed_slns[row-my_weight][col-1],
                                                  computed_slns[row][col-1])

                # weight of item does not fit, so this solution is same as the previous item
                else:
                    computed_slns[row][col] = computed_slns[row][col-1]

        optimal_value = computed_slns[self.weight_capacity][self.n]

        if self.log:
            print(" Computed Solutions Array: ")
            for row in range(self.weight_capacity + 1):
                for col in range(self.n + 1):
                    if col == 0:
                        print("\t[", computed_slns[row][col], end=", ")
                    elif col != self.n:
                        print(computed_slns[row][col], end=", ")
                    else:
                        print(computed_slns[row][col], end="]\n")

            print("\nOptimal Value: ", optimal_value, "\n")

        return optimal_value
