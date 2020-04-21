# Import packages.
import numpy as np
import matplotlib.pyplot as plt


#
# Static functions.
#

def check_occupied(occupancy_mat, team_id, idx, duration):
    dim = occupancy_mat.shape
    end_idx = idx + duration if idx + duration < dim[1] else dim[1]
    occupied_sum = occupancy_mat[team_id, idx:end_idx].sum()
    return occupied_sum > 0


def set_occupied(occupancy_mat, team_id, idx, duration):
    dim = occupancy_mat.shape
    end_idx = idx + duration if idx + duration < dim[1] else dim[1]
    occupancy_mat[team_id, idx:end_idx] = np.ones((1, end_idx - idx))


class GeneticAlgorithm:
    #
    # Attributes.
    #

    tasks = None

    n_time_slots_cycle = None
    n_time_slots_task = None
    n_task = None
    n_chromo_len = None
    n_teams = None

    n_iterations = None
    n_crossover = None
    n_mutate = None

    n_chromosomes = None
    chromosomes = None
    parents_1 = None
    parents_2 = None
    fitness_values = None
    chromo_size = None

    empty_team_id = None

    results_fitness = None

    sim_results_best_fitness = None
    sim_results_mean_fitness = None

    #
    # Methods.
    #

    def __init__(self, param, tasks_in):
        # Set parameters.
        self.random_seed = param.RAND_SEED

        self.n_time_slots_cycle = param.N_TIME_SLOTS_CYCLE
        self.n_time_slots_task = param.N_TIME_SLOTS_TASK
        self.n_task = param.N_TASKS
        self.n_chromo_len = param.N_CHROMOSOME_LENGTH
        self.n_chromosomes = param.N_CHROMOSOMES
        self.chromo_size = (self.n_chromosomes, self.n_chromo_len)

        self.n_teams = param.N_TEAMS

        self.n_iterations = param.N_ITERATIONS
        self.n_crossover = param.N_CROSSOVER
        self.n_mutate = param.N_MUTATE

        self.empty_team_id = param.EMTPY_TEAM_ID

        self.n_randomized_sim = param.N_RANDOMIZED_SIM

        # Save tasks.
        self.tasks = tasks_in

        # Initialize empty chromosomes as a double int array.
        self.chromosomes = [self.empty_team_id * np.ones(self.chromo_size, dtype=np.int),
                            self.empty_team_id * np.ones(self.chromo_size, dtype=np.int)]

        # Initialize fitness values.
        self.fitness_values = np.zeros(self.n_chromosomes)

        # Initialize parents.
        self.parents_1 = np.zeros(self.n_chromosomes, dtype=np.int)
        self.parents_2 = np.zeros(self.n_chromosomes, dtype=np.int)

        # Initialize result variables.
        self.results_fitness = np.zeros((self.n_chromosomes, self.n_iterations))

        self.sim_results_best_fitness = np.zeros((self.n_randomized_sim, self.n_iterations))
        self.sim_results_mean_fitness = np.zeros((self.n_randomized_sim, self.n_iterations))

    def initialize_chromosomes(self):
        """
        Initialization of the chromosomes by random values, then ensure feasibility.
        """
        # Generate random chromosomes.
        for i in range(self.n_chromosomes):
            random_chromosome = self.generate_random_chromosome()
            self.chromosomes[0][i, :] = random_chromosome[0]
            self.chromosomes[1][i, :] = random_chromosome[1]

        self.repair_chromosomes()

    def select_chromosomes(self):
        # Generate cumulative probability for selection process.
        positive_fitness_values = self.fitness_values.clip(0)
        cum_fitness = np.cumsum(positive_fitness_values, axis=0)

        # Pick parent indices with proportional probability to their fitness.
        for i in range(self.n_chromosomes):
            rand1 = np.random.uniform(0, 1) * cum_fitness[-1]
            rand2 = np.random.uniform(0, 1) * cum_fitness[-1]
            parent_1_idx = np.argmax(cum_fitness >= rand1)
            parent_2_idx = np.argmax(cum_fitness >= rand2)
            self.parents_1[i] = parent_1_idx
            self.parents_2[i] = parent_2_idx

    def crossover(self):
        # Initialize empty chromosomes as a double int array.
        new_chromo_size = (self.n_crossover, self.n_chromo_len)
        new_chromosomes = [self.empty_team_id * np.zeros(new_chromo_size, dtype=np.int),
                           self.empty_team_id * np.ones(new_chromo_size, dtype=np.int)]

        for i in range(self.n_crossover):
            for j in range(self.n_chromo_len):
                # Parent indices.
                p_idx_1 = self.parents_1[i]
                p_idx_2 = self.parents_2[i]

                # Crossover time slot.
                t1 = self.chromosomes[0][p_idx_1, j]
                t2 = self.chromosomes[0][p_idx_2, j]
                d_t = np.abs(t1 - t2)
                t_rand = np.random.uniform(t1 - d_t / 2.0, t2 + d_t / 2.0)
                t_rand = min(self.n_time_slots_cycle - 1, max(round(t_rand), 0))
                new_chromosomes[0][i, j] = t_rand

                # Crossover team id.
                rand_team_idx = p_idx_1 if np.random.uniform(0, 1) < 0.5 else p_idx_2
                team_id = self.chromosomes[1][rand_team_idx, j]
                new_chromosomes[1][i, j] = team_id

        # Replace least fit chromosomes with new chromosomes.
        self.chromosomes[0][0:self.n_crossover, :] = new_chromosomes[0]
        self.chromosomes[1][0:self.n_crossover, :] = new_chromosomes[1]

    def mutate(self):
        # Range of chromosomes allowed to mutate.
        min_index = int(round(0 * self.n_chromosomes))
        max_index = int(round(0.8 * self.n_chromosomes))

        # Mutate chromosomes.
        for i in range(self.n_mutate):
            rand_chromosome_idx = np.random.random_integers(min_index, max_index)
            rand_gene_idx = np.random.random_integers(0, self.n_chromo_len - 1)
            time_slot = np.random.random_integers(0, self.n_time_slots_cycle - 1)
            team_id = np.random.random_integers(-1, self.n_teams - 1)
            self.chromosomes[0][rand_chromosome_idx, rand_gene_idx] = time_slot
            self.chromosomes[1][rand_chromosome_idx, rand_gene_idx] = team_id

    def mutate2(self):
        # Range of chromosomes allowed to mutate.
        min_index = int(round(0 * self.n_chromosomes))
        max_index = int(round(0.8 * self.n_chromosomes))

        # Mutate chromosomes.
        for i in range(self.n_mutate):
            rand_chromosome_idx = np.random.random_integers(min_index, max_index)
            rand_gene_idx = np.random.random_integers(0, self.n_chromo_len - 1)
            old_time_slot = self.chromosomes[0][rand_chromosome_idx, rand_gene_idx]
            time_slot = old_time_slot + 1 if np.random.uniform(0, 1) < 0.5 else old_time_slot - 1
            time_slot = min(self.n_time_slots_cycle - 1, max(int(round(time_slot)), 0))
            team_id = np.random.random_integers(-1, self.n_teams - 1)
            self.chromosomes[0][rand_chromosome_idx, rand_gene_idx] = time_slot
            self.chromosomes[1][rand_chromosome_idx, rand_gene_idx] = team_id

    def repair_chromosomes(self):
        # Correct for feasible schedules and compute fitness.
        for i in range(self.n_chromosomes):
            # Occupancy table to identify infeasible schedules.
            team_occupancy = np.zeros((self.n_teams, self.n_time_slots_cycle), dtype=np.int)
            self.ensure_feasibility([self.chromosomes[0][i, :], self.chromosomes[1][i, :]], team_occupancy)
            self.fitness_values[i] = self.compute_fitness_value(i, team_occupancy)

        self.sort_chromosomes_by_fitness()

    def start(self):
        for i_sim in range(0, self.n_randomized_sim):
            print ("\n\nSimulation %d" % i_sim)
            # Seed random value.
            np.random.seed(self.random_seed + i_sim)

            # Initialize Chromosomes.
            self.initialize_chromosomes()

            for i in range(self.n_iterations):
                # Select and save parents.
                self.select_chromosomes()

                # Genetic operator: crossover.
                self.crossover()

                # Genetic operator: mutate.
                self.mutate2()

                # Repair schedules to be feasible.
                self.repair_chromosomes()

                # Save results.
                self.results_fitness[:, i] = self.fitness_values
                print ("Iteration %d" % i)

            # Compute results.
            self.sim_results_mean_fitness[i_sim, :] = self.results_fitness.mean(axis=0)
            self.sim_results_best_fitness[i_sim, :] = self.results_fitness[-1, :]

            # print("--------")
            # print(i)
            # print(self.fitness_values)
            # print(self.fitness_values.mean())
            # print

    def plot_results(self):
        # Plot results.
        plt.ioff()
        fig, ax = plt.subplots()  # Create a figure containing a single axes.

        # for i in range(0,self.n_randomized_sim):
        #     ax.plot(np.arange(1, self.n_iterations+1), self.sim_results_best_fitness[i,:])
        #     ax.plot(np.arange(1, self.n_iterations+1), self.sim_results_mean_fitness[i,:])

        # Plot confidence interval.
        mu_best_fitness = self.sim_results_best_fitness.mean(axis=0)
        mu_mean_fitness = self.sim_results_mean_fitness.mean(axis=0)
        sigma_best_fitness = self.sim_results_best_fitness.std(axis=0)
        sigma_mean_fitness = self.sim_results_mean_fitness.std(axis=0)

        ax.fill_between(np.arange(1, self.n_iterations + 1),
                        (mu_best_fitness - sigma_best_fitness),
                        (mu_best_fitness + sigma_best_fitness), alpha=0.2, label="Confidence Max Fitness (1 std)")

        ax.fill_between(np.arange(1, self.n_iterations + 1),
                        (mu_mean_fitness - sigma_mean_fitness),
                        (mu_mean_fitness + sigma_mean_fitness), alpha=0.2, label="Confidence Mean Fitness (1 std)")

        # Plot last simulation.
        ax.plot(np.arange(1, self.n_iterations + 1), self.results_fitness[-1, :], label="Fitness Max")
        ax.plot(np.arange(1, self.n_iterations + 1), self.results_fitness.mean(axis=0), label="Fitness Mean")

        # Configure plot appearance.
        ax.set_xlabel("Iteration")
        ax.set_ylabel("Average and Max Fitness")
        ax.grid(True)
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.9))
        fig.subplots_adjust(right=0.625)  # Try to fit the legend box located outside.
        fig.set_figwidth(8)  # In inches.
        ax.set_title("Fitness Values")
        plt.show()

    def generate_random_chromosome(self):
        # Initialize time slots.
        N_slots_cycle = self.n_time_slots_cycle
        N_slots_task = self.n_time_slots_task

        chromosome = [self.empty_team_id * np.ones(self.n_chromo_len, dtype=np.int),
                      self.empty_team_id * np.ones(self.n_chromo_len, dtype=np.int)]

        # Random time slots, sorted in ascending order.
        for j in range(self.n_task):
            rand_row = np.random.random_integers(0, N_slots_cycle - 1, (1, N_slots_task))
            rand_row = np.sort(rand_row)
            chromosome[0][j * N_slots_task:(j + 1) * N_slots_task] = rand_row

        # Random team IDs.
        rand_row = np.random.random_integers(0, self.n_teams - 1, self.n_chromo_len)
        chromosome[1] = rand_row

        return chromosome

    def ensure_feasibility(self, schedule, team_occupancy):
        # Iterate through the schedule and remove double missions on the same time slot.
        for i in range(1, self.n_time_slots_task):
            for j in range(self.n_task):
                idx_gene = i + j * self.n_time_slots_task
                if schedule[0][idx_gene] == schedule[0][idx_gene - 1] and \
                        schedule[1][idx_gene - 1] != self.empty_team_id:
                    schedule[1][idx_gene] = self.empty_team_id

        # Iterate through time slots in tasks and remove resource conflicts.
        for i in range(self.n_time_slots_task):
            for j in range(self.n_task):
                idx_gene = i + j * self.n_time_slots_task
                idx_time_slot = schedule[0][idx_gene]
                team_id = schedule[1][idx_gene]
                # Check if any team is assigned for the time slot.
                # If not occupied, set occupied. Else, cancel the task.
                is_occupied = check_occupied(team_occupancy, team_id, idx_time_slot, self.tasks[j].duration_execution)
                if team_id != self.empty_team_id and not is_occupied:
                    set_occupied(team_occupancy, team_id, idx_time_slot, self.tasks[j].duration_execution)
                elif team_id != self.empty_team_id and is_occupied:
                    schedule[1][idx_gene] = self.empty_team_id

    def compute_fitness_value(self, idx_chromosome, team_occupancy):
        fitness_value = 0

        # Compute fitness value from task constraints.
        for i in range(self.n_task):
            N_slots = self.n_time_slots_task
            f_i = self.tasks[i].fitness([self.chromosomes[0][idx_chromosome, i * N_slots:(i + 1) * N_slots],
                                         self.chromosomes[1][idx_chromosome, i * N_slots:(i + 1) * N_slots]],
                                        self.empty_team_id, self.n_time_slots_cycle)
            fitness_value = fitness_value + f_i.mean()

        # Compute fitness value from resource usage.
        sum_occupancy = np.sum(team_occupancy, axis=1)
        mean_sum_occupancy = sum_occupancy.mean()
        f_team = 1.0 - np.abs((sum_occupancy - mean_sum_occupancy) / mean_sum_occupancy)
        fitness_value = fitness_value + f_team.mean()

        return fitness_value

    def compute_fitness_vector(self, schedule, team_occupancy):
        fitness_value = []

        # Compute fitness value from task constraints.
        for i in range(self.n_task):
            N_slots = self.n_time_slots_task
            f_i = self.tasks[i].fitness([schedule[0][i * N_slots:(i + 1) * N_slots],
                                         schedule[1][i * N_slots:(i + 1) * N_slots]],
                                        self.empty_team_id, self.n_time_slots_cycle)
            fitness_value.append(f_i)

        # Compute fitness value from resource usage.
        sum_occupancy = np.sum(team_occupancy, axis=1)
        mean_sum_occupancy = sum_occupancy.mean()
        f_team = 1.0 - np.abs((sum_occupancy - mean_sum_occupancy) / mean_sum_occupancy)
        fitness_value.append(f_team)

        return fitness_value

    def sort_chromosomes_by_fitness(self):
        sorted_idx_vec = np.argsort(self.fitness_values)
        self.fitness_values = self.fitness_values[sorted_idx_vec]
        self.chromosomes[0] = self.chromosomes[0][sorted_idx_vec, :]
        self.chromosomes[1] = self.chromosomes[1][sorted_idx_vec, :]

    def print_schedule(self, schedule):
        # Generate schedule in array.
        time_table = self.empty_team_id * np.ones((self.n_task, self.n_time_slots_cycle), dtype=np.int)
        for i in range(self.n_time_slots_task):
            for j in range(self.n_task):
                idx_gene = i + j * self.n_time_slots_task
                idx_time_slot = schedule[0][idx_gene]
                team_id = schedule[1][idx_gene]
                if time_table[j, idx_time_slot] == self.empty_team_id:
                    time_table[j, idx_time_slot] = team_id

        # header_time_table = np.zeros((self.n_task + 1, self.n_time_slots_cycle), dtype=np.int)
        # header_time_table[0, :] = np.arange(self.n_time_slots_cycle)
        # header_time_table[1:self.n_task + 1, :] = time_table
        #
        # # Remove empty elements.
        # str_time_table = str(header_time_table)
        # str_time_table = str_time_table.replace(str(self.empty_team_id), "--")
        #
        # print str_time_table
        #
        print_str = "         " + str(np.arange(self.n_time_slots_cycle)) + "\n"
        for i in range(0, time_table.shape[0]):
            task_str = "Task %2d: " % i
            next_str = np.array2string(time_table[i, :], formatter={'int_kind': lambda x: "%2d" % x})
            next_str = next_str.replace("-1", "--")
            print_str += task_str + next_str + "\n"
        print(print_str)

    def print_team_time_slots(self, idx):
        print("\nFitness: {0}".format(self.fitness_values[idx]))
        print("Task schedule:")
        self.print_schedule([self.chromosomes[0][idx], self.chromosomes[1][idx]])

        print ("\nTeam time slots of best schedule:")
        team_occupancy = np.zeros((self.n_teams, self.n_time_slots_cycle), dtype=np.int)
        self.ensure_feasibility([self.chromosomes[0][idx, :], self.chromosomes[1][idx, :]], team_occupancy)

        print_str = "         " + str(np.arange(self.n_time_slots_cycle)) + "\n"
        for i in range(0, team_occupancy.shape[0]):
            team_str = "Team %2d: " % i
            next_str = np.array2string(team_occupancy[i, :], formatter={'int_kind': lambda x: "%2d" % x})
            next_str = next_str.replace(" 0", "--")
            next_str = next_str.replace("1", "x")
            print_str += team_str + next_str + "\n"
        print(print_str)
