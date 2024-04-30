import random

from simulationObjects.Worker import Worker
from simulationObjects.Task import Task

def simulation(task_list,workers, scheduler):
    sumOfTAT = .0
    number_tasks = .0
    durations = []

    scheduled_tasks = scheduler.schedule(task_list, workers)


    for idx, worker_tasks in enumerate(scheduled_tasks):
        if len(worker_tasks) > 0:
            number_tasks += len(worker_tasks)
            sumOfTAT += len(worker_tasks) * workers[idx].compute_mTAT(worker_tasks)
            durations.append(workers[idx].compute_duration(worker_tasks))
    thruput = float(number_tasks)/max(durations)
    return sumOfTAT/number_tasks, thruput

def run_simulation(worker_speeds, max_num_tasks, num_simulations, scheduler, random_seed):
    # Initialize random
    random.seed(random_seed)

    # Initialize workers
    worker_list = [Worker(speed) for speed in worker_speeds]

    # Varying number of tasks
    num_tasks_list = list(range(50, max_num_tasks + 1, 5))
    avg_mTATs = []
    avg_thruputs = []

    for num_tasks in num_tasks_list:
        task_list = [Task(random.randint(1, 100)) for _ in range(num_tasks)]  # Generating random tasks

        simulation_mTATs = []
        simulation_thruputs = []

        # Generate a random seed for this simulation
        random_seed = random.randint(0, 1000000)
        random.seed(random_seed)

        for _ in range(num_simulations):
            # Perform simulations for the scheduler
            mTAT, thruput = simulation(task_list, worker_list, scheduler)
            simulation_mTATs.append(mTAT)
            simulation_thruputs.append(thruput)

        avg_mTAT = sum(simulation_mTATs) / len(simulation_mTATs)
        avg_mTATs.append(avg_mTAT)
        avg_thruput = sum(simulation_thruputs) / len(simulation_thruputs)
        avg_thruputs.append(avg_thruput)

    return num_tasks_list, avg_mTATs, avg_thruputs
