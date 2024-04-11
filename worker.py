import random
import matplotlib.pyplot as plt

class Task:
    def __init__(self, task_size):
        self.task_size = task_size

class Worker:
    def __init__(self, w_speed):
        self.w_speed = w_speed

    def computeTime(self,task):
        return task.task_size/self.w_speed

    def compute_mTAT(self,tasks):
        total_duration = 0
        sum_TAT = 0
        for task in tasks:
            sum_TAT += total_duration + self.computeTime(task)
            total_duration += self.computeTime(task)
        return sum_TAT/len(tasks)

class FIFO_Scheduler():
    def complexity(self, n):
        return n
    def constant_penalties(self):
        return 0
    def schedule(self,tasks,workers):
        # Initialize an empty matrix to store the scheduled tasks
        result_matrix = [[] for _ in range(len(workers))]

        # Schedule using FIFO
        for id,task in enumerate(tasks):
            result_matrix[id%len(workers)].append(task)

        return result_matrix

class TaskEstimator_Scheduler():
    def complexity(self, n):
        return n
    def constant_penalties(self):
        return 0
    def schedule(self,tasks,workers):
        # Initialize an empty matrix to store the scheduled tasks
        result_matrix = [[] for _ in range(len(workers))]

        # Initialize a list of tuples to keep track of the number of tasks scheduled on each worker
        task_counts = [[id, 0] for id in range(len(workers))]  # Each tuple represents (worker_id, task_count)

        # Schedule using FIFO
        for id,task in enumerate(tasks):
            # Sort workers based on their task counts
            sorted_workers = sorted(task_counts, key=lambda x: x[1])

            result_matrix[sorted_workers[0][0]].append(task)
            sorted_workers[0][1] += task.task_size

        return result_matrix

def simulation(task_list,workers, scheduler):
    sumOfTAT = 0
    number_tasks = 0

    scheduled_tasks = scheduler.schedule(task_list, worker_list)


    for idx, worker_tasks in enumerate(scheduled_tasks):
        if len(worker_tasks) > 0:
            number_tasks += len(worker_tasks)
            sumOfTAT += len(worker_tasks) * workers[idx].compute_mTAT(worker_tasks)
    return sumOfTAT/number_tasks
    
if __name__ == "__main__":
    # Simulation configuration
    worker_speeds = [1, 1, 1, 1,1, 1, 1, 1,1, 1, 1, 1,1, 1, 1, 1,1, 1, 1, 1,1, 1, 1, 1,1, 1, 1, 1,1, 1, 1, 1]  # Speeds of workers
    num_workers = len(worker_speeds)  # Number of workers
    worker_list = [Worker(speed) for speed in worker_speeds]  # Generating workers with predefined speeds

    max_num_tasks = 100 # minimum of 50
    num_simulations = 10

    # Initialize schedulers
    fifo_scheduler = FIFO_Scheduler()
    task_estimator_scheduler = TaskEstimator_Scheduler()

    # How relevant is the scheduling complexity of the algorithm
    complexity_coefficient = 0.01

    # Varying number of tasks
    num_tasks_list = list(range(50, max_num_tasks + 1, 5))
    avg_results_fifo = []
    avg_results_task_estimator = []

    for num_tasks in num_tasks_list:
        task_list = [Task(random.randint(1, 100)) for _ in range(num_tasks)]  # Generating random tasks

        fifo_simulation_results = []
        task_estimator_simulation_results = []

        for _ in range(num_simulations):
            # Perform simulations for both schedulers
            fifo_result = simulation(task_list, worker_list, fifo_scheduler)
            fifo_simulation_results.append(fifo_result)

            task_estimator_result = simulation(task_list, worker_list, task_estimator_scheduler)
            task_estimator_simulation_results.append(task_estimator_result)

        avg_fifo_result = sum(fifo_simulation_results) / len(fifo_simulation_results)
        avg_results_fifo.append(avg_fifo_result)

        avg_task_estimator_result = sum(task_estimator_simulation_results) / len(task_estimator_simulation_results)
        avg_results_task_estimator.append(avg_task_estimator_result)

    # Plotting
    plt.plot(num_tasks_list, avg_results_fifo, marker='o', label='FIFO Scheduler')
    plt.plot(num_tasks_list, avg_results_task_estimator, marker='o', label='Task Estimator Scheduler')
    plt.title('Average Simulation TAT vs Number of Tasks')
    plt.xlabel('Number of Tasks')
    plt.ylabel('Average TA Time Result')
    plt.legend()
    plt.grid(True)
    plt.show()
