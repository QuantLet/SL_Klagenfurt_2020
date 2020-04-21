# Import packages.
import numpy as np


class Task:
    #
    # Attributes.
    #

    task_name = None
    duration_execution = None
    duration_next = None
    n_max_task = None

    #
    # Methods.
    #

    def fitness(self, schedule, empty_team_id, n_time_slots_cycle):
        fitness_value = np.zeros(2)

        # Remove emtpy schedule entries.
        non_empty_slots = schedule[1] != empty_team_id
        non_empty_schedule = [schedule[0][non_empty_slots], schedule[1][non_empty_slots]]

        # Ideal distribution of execution times.
        if non_empty_schedule[0].shape[0] <= 1:
            fitness_value[0] = 0
        else:
            # Time distance between schedule elements.
            # The time distance of duration_next is ideal and gives f_1 = 1 (100%).
            diff = non_empty_schedule[0][1:] - non_empty_schedule[0][0:-1]
            f_1 = (self.duration_next - diff) / float(self.duration_next)
            f_1 = 1.0 - np.abs(f_1)
            # f_1 = f_1.clip(0) # Restrict to positive values.
            # Value can be negative to penalize bad distribution.

            # Time distance to the start and end of planning cycle.
            # The schedule starting at 0 is ideal and gives f_cycle = 1 (100%).
            f_cycle = non_empty_schedule[0][0] / float(self.duration_next)
            f_cycle = 1.0 - np.abs(f_cycle)
            f_1 = np.append(f_1, f_cycle)

            # The schedule ending at (n_time_slots_cycle - duration_next) is ideal
            # and gives f_cycle = 1 (100%).
            diff_end = n_time_slots_cycle - non_empty_schedule[0][-1]
            f_cycle = (self.duration_next - diff_end) / float(self.duration_next)
            f_cycle = 1.0 - np.abs(f_cycle)
            f_1 = np.append(f_1, f_cycle)

            f_1 = f_1.mean()
            fitness_value[0] = f_1

        # Ideal number of executions in cycle.
        N_non_empty = non_empty_schedule[0].shape[0]
        f_2 = 1.0 - np.abs((self.n_max_task - N_non_empty) / float(self.n_max_task))
        fitness_value[1] = f_2

        return fitness_value

    def __init__(self, name, d1, d2, n1):
        self.task_name = name
        self.duration_execution = d1
        self.duration_next = d2
        self.n_max_task = n1