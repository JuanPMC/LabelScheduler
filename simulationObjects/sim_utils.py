import random

from sumulationObjects.Worker import Worker
from sumulationObjects.Task import Task

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