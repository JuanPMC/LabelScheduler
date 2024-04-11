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
    
class MTAT_Scheduler():
    def complexity(self, n):
        return n
    def constant_penalties(self):
        return 0
    
    def mTAT(self,mean_duration, mean_speed, n_tasks):
        return (mean_duration / mean_speed) * (n_tasks * (n_tasks + 1) / 2)

    def schedule(self,tasks,workers):
        scores = []
        task_sizes = [task.task_size for task in tasks]
        mean_task_size = float(sum(task_sizes)) / float(len(task_sizes))

        for id, worker in enumerate(workers):
            for i in range(len(tasks)):
                if mean_task_size != 0:
                    scores.append([id, 20 * (self.mTAT(mean_task_size, worker.w_speed, i+1))**(-1)])
                else:
                    mean_task_size = 1
        scores.sort(key=lambda x: x[1], reverse=True)

        # Initialize an empty matrix to store the scheduled tasks
        result_matrix = [[] for _ in range(len(workers))]

        # Initialize a list of tuples to keep track of the number of tasks scheduled on each worker
        task_counts = [[id, 0] for id in range(len(workers))]  # Each tuple represents (worker_id, task_count)

        # Schedule using FIFO
        for id,task in enumerate(tasks):
            result_matrix[scores[id][0]].append(task)

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
            
class TaskEstimatorHomo_Scheduler():
    def complexity(self, n):
        return n
    def constant_penalties(self):
        return 0
    def schedule(self,tasks,workers):
        # Initialize an empty matrix to store the scheduled tasks
        result_matrix = [[] for _ in range(len(workers))]

        # Initialize a list of tuples to keep track of the number of tasks scheduled on each worker
        task_counts = [[id, 0] for id in range(len(workers))]  # Each tuple represents (worker_id, task_count)

        # Schedule
        for id,task in enumerate(tasks):
            # Sort workers based on their task counts
            sorted_workers = sorted(task_counts, key=lambda x: x[1])

            result_matrix[sorted_workers[0][0]].append(task)
            sorted_workers[0][1] += (1/workers[sorted_workers[0][0]].w_speed) * task.task_size
        
        return result_matrix
    
class SimpleLoop_Scheduler():
    def complexity(self, n):
        return n
    def constant_penalties(self):
        return 0
    def schedule(self,tasks,workers):
        # Initialize an empty matrix to store the scheduled tasks
        result_matrix = [[] for _ in range(len(workers))]

        # Initialize a list of tuples to keep track of the number of tasks scheduled on each worker
        worker_speeds = [[id, worker.w_speed] for id, worker in enumerate(workers)]  # Each tuple represents (worker_id, task_count)

        # Sort workers based on their task counts
        sorted_workers = sorted(worker_speeds, key=lambda x: -x[1])

        # Schedule
        for id,task in enumerate(tasks):
            result_matrix[sorted_workers[0][0]].append(task)
        
        return result_matrix

def simulation(task_list,workers, scheduler):
    sumOfTAT = 0
    number_tasks = 0

    scheduled_tasks = scheduler.schedule(task_list, workers)


    for idx, worker_tasks in enumerate(scheduled_tasks):
        if len(worker_tasks) > 0:
            number_tasks += len(worker_tasks)
            sumOfTAT += len(worker_tasks) * workers[idx].compute_mTAT(worker_tasks)
    return sumOfTAT/number_tasks

def run_simulation(worker_speeds, max_num_tasks, num_simulations, scheduler, random_seed):
    # Initialize random
    random.seed(random_seed)

    # Initialize workers
    worker_list = [Worker(speed) for speed in worker_speeds]

    # Varying number of tasks
    num_tasks_list = list(range(50, max_num_tasks + 1, 5))
    avg_results = []

    for num_tasks in num_tasks_list:
        task_list = [Task(random.randint(1, 100)) for _ in range(num_tasks)]  # Generating random tasks

        simulation_results = []

        # Generate a random seed for this simulation
        random_seed = random.randint(0, 1000000)
        random.seed(random_seed)

        for _ in range(num_simulations):
            # Perform simulations for the scheduler
            result = simulation(task_list, worker_list, scheduler)
            simulation_results.append(result)

        avg_result = sum(simulation_results) / len(simulation_results)
        avg_results.append(avg_result)

    return num_tasks_list, avg_results


if __name__ == "__main__":

    # Simulation configuration
    worker_speeds = [1] * 4
    max_num_tasks = 100  # maximum number of tasks
    num_simulations = 10

    # Generate a random seed
    random_seed = random.randint(1, 100)

    # Initialize schedulers
    fifo_scheduler = FIFO_Scheduler()
    task_estimator_scheduler = TaskEstimator_Scheduler()
    task_estimator_scheduler_homo = TaskEstimatorHomo_Scheduler()
    mtat_scheduler = MTAT_Scheduler()
    simple_scheduler = SimpleLoop_Scheduler()

    # Run simulation with FIFO Scheduler
    num_tasks_list_fifo, avg_results_fifo = run_simulation(worker_speeds, max_num_tasks, num_simulations, fifo_scheduler,random_seed)

    # Run simulation with Task Estimator Scheduler
    num_tasks_list_task_estimator, avg_results_task_estimator = run_simulation(worker_speeds, max_num_tasks, num_simulations, task_estimator_scheduler,random_seed)

    # Run simulation with Task Estimator Homo Scheduler
    num_tasks_list_task_estimator_homo, avg_results_task_estimator_homo = run_simulation(worker_speeds, max_num_tasks, num_simulations, task_estimator_scheduler_homo,random_seed)

    # Run simulation with MTAT
    num_tasks_list_mtat, avg_results_mtat = run_simulation(worker_speeds, max_num_tasks, num_simulations, mtat_scheduler,random_seed)

    # Run simulation with SimpleLoop
    num_tasks_list_simple, avg_results_simple = run_simulation(worker_speeds, max_num_tasks, num_simulations, simple_scheduler,random_seed)

    # Plotting
    plt.plot(num_tasks_list_fifo, avg_results_fifo, marker='o', label='FIFO Scheduler')
    plt.plot(num_tasks_list_task_estimator, avg_results_task_estimator, marker='o', label='Task Estimator Scheduler')
    plt.plot(num_tasks_list_task_estimator_homo, avg_results_task_estimator_homo, marker='o', label='Task Estimator Homo Scheduler')
    plt.plot(num_tasks_list_mtat, avg_results_mtat, marker='o', label='mTAT')
    plt.plot(num_tasks_list_simple, avg_results_simple, marker='o', label='Simple loop')

    plt.title('Average Simulation TAT vs Number of Tasks')
    plt.xlabel('Number of Tasks')
    plt.ylabel('Average TA Time Result')
    plt.legend()
    plt.grid(True)
    plt.show()
