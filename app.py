import random
import matplotlib.pyplot as plt
from schedulers.FIFO_Scheduler import FIFO_Scheduler
from schedulers.TaskEstimator_Scheduler import TaskEstimator_Scheduler
from schedulers.TaskEstimatorHomo_Scheduler import TaskEstimatorHomo_Scheduler
from schedulers.MTAT_Scheduler import MTAT_Scheduler
from schedulers.SimpleLoop_Scheduler import SimpleLoop_Scheduler
from simulationObjects.sim_utils import run_simulation


if __name__ == "__main__":

    # Simulation configuration
    worker_speeds = [1] * 100 + [2] * 100
    max_num_tasks = 1000  # maximum number of tasks
    num_simulations = 10

    # Generate a random seed
    random_seed = random.randint(1, 100)

    # Initialize schedulers
    fifo_scheduler = FIFO_Scheduler()
    task_estimator_scheduler = TaskEstimator_Scheduler()
    task_estimator_scheduler_homo = TaskEstimatorHomo_Scheduler()
    mtat_scheduler = MTAT_Scheduler()
    #simple_scheduler = SimpleLoop_Scheduler()

    # Run simulation with FIFO Scheduler
    num_tasks_list_fifo, avg_results_fifo = run_simulation(worker_speeds, max_num_tasks, num_simulations, fifo_scheduler,random_seed)

    # Run simulation with Task Estimator Scheduler
    num_tasks_list_task_estimator, avg_results_task_estimator = run_simulation(worker_speeds, max_num_tasks, num_simulations, task_estimator_scheduler,random_seed)

    # Run simulation with Task Estimator Homo Scheduler
    num_tasks_list_task_estimator_homo, avg_results_task_estimator_homo = run_simulation(worker_speeds, max_num_tasks, num_simulations, task_estimator_scheduler_homo,random_seed)

    # Run simulation with MTAT
    num_tasks_list_mtat, avg_results_mtat = run_simulation(worker_speeds, max_num_tasks, num_simulations, mtat_scheduler,random_seed)

    # # Run simulation with SimpleLoop
    # num_tasks_list_simple, avg_results_simple = run_simulation(worker_speeds, max_num_tasks, num_simulations, simple_scheduler,random_seed)

    # Plotting
    plt.plot(num_tasks_list_fifo, avg_results_fifo, marker='o', label='FIFO Scheduler')
    plt.plot(num_tasks_list_task_estimator, avg_results_task_estimator, marker='o', label='Task Estimator Scheduler')
    plt.plot(num_tasks_list_task_estimator_homo, avg_results_task_estimator_homo, marker='o', label='Task Estimator Homo Scheduler')
    plt.plot(num_tasks_list_mtat, avg_results_mtat, marker='o', label='mTAT')
  #  plt.plot(num_tasks_list_simple, avg_results_simple, marker='o', label='Simple loop')

    plt.title('Average Simulation TAT vs Number of Tasks')
    plt.xlabel('Number of Tasks')
    plt.ylabel('Average TA Time Result')
    plt.legend()
    plt.grid(True)
    plt.show()
