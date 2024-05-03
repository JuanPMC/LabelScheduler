import random
import matplotlib.pyplot as plt
from schedulers.FIFO_Scheduler import FIFO_Scheduler
from schedulers.Optimal_scheduler import Optima_Scheduler
from schedulers.LoadEstimator_Scheduler import LoadEstimator_Scheduler
from schedulers.LoadEstimatorHomo_Scheduler import LoadEstimatorHomo_Scheduler
from schedulers.thuput_Scheduler import thuput_Scheduler
from schedulers.MTAT_Scheduler import MTAT_Scheduler
from schedulers.AllInBest import AllInBest
from simulationObjects.sim_utils import run_simulation


if __name__ == "__main__":

    # Simulation configuration
    worker_speeds = [1] * 100 + [2] * 100
    max_num_tasks = 300  # maximum number of tasks
    num_simulations = 10

    # Generate a random seed
    random_seed = random.randint(1, 100)

    # Initialize schedulers
    fifo_scheduler = FIFO_Scheduler()
    load_estimator_scheduler = LoadEstimator_Scheduler()
    load_estimator_scheduler_homo = LoadEstimatorHomo_Scheduler()
    thuput_Scheduler = thuput_Scheduler()
    mtat_scheduler = MTAT_Scheduler()
    #all_in_best = AllInBest()
    optima_sch = Optima_Scheduler()

    # Run simulation with FIFO Scheduler
    num_tasks_list_fifo, avg_results_fifo, avg_thruputs_fifo = run_simulation(worker_speeds, max_num_tasks, num_simulations, fifo_scheduler,random_seed)

    # Run simulation with Task Estimator Scheduler
    num_tasks_list_task_estimator, avg_results_task_estimator, avg_thruputs_task_estimator = run_simulation(worker_speeds, max_num_tasks, num_simulations, load_estimator_scheduler,random_seed)

    # Run simulation with Task Estimator Homo Scheduler
    num_tasks_list_task_estimator_homo, avg_results_task_estimator_homo,task_estimator_homo = run_simulation(worker_speeds, max_num_tasks, num_simulations, load_estimator_scheduler_homo,random_seed)

    # Run simulation with thruput
    num_tasks_list_thruput, avg_results_thruput, avg_thruputs_thruput = run_simulation(worker_speeds, max_num_tasks, num_simulations, thuput_Scheduler,random_seed)

    # Run simulation with MTAT
    num_tasks_list_mtat, avg_results_mtat, avg_thruputs_mtat  = run_simulation(worker_speeds, max_num_tasks, num_simulations, mtat_scheduler,random_seed)
    
    # Run simulation with optimal
    num_tasks_list_optimal, avg_results_optimal, avg_thruputs_optimal  = run_simulation(worker_speeds, max_num_tasks, num_simulations, optima_sch,random_seed)

    # # Run simulation with SimpleLoop
    # num_tasks_list_simple, avg_results_simple = run_simulation(worker_speeds, max_num_tasks, num_simulations, all_in_best,random_seed)

    # Plotting
    plt.plot(num_tasks_list_fifo, avg_thruputs_fifo, marker='o', label='FIFO Scheduler')
    plt.plot(num_tasks_list_task_estimator, avg_thruputs_task_estimator, marker='o', label='Task Estimator Scheduler')
    plt.plot(num_tasks_list_task_estimator_homo, task_estimator_homo, marker='o', label='Task Estimator Heterogeneus Scheduler')
    plt.plot(num_tasks_list_thruput, avg_thruputs_thruput, marker='o', label='Thurput Scheduler')
    plt.plot(num_tasks_list_mtat, avg_thruputs_mtat, marker='o', label='mTAT')
    plt.plot(num_tasks_list_optimal, avg_thruputs_optimal, marker='o', label='Optimal')


  #  plt.plot(num_tasks_list_simple, avg_results_simple, marker='o', label='Simple loop')

    plt.title('Average Throughput vs Number of Tasks')
    plt.xlabel('Number of Tasks')
    plt.ylabel('Average Throughput Result')
    plt.legend()
    plt.grid(True)
    plt.show()
    
  # Plotting TaT --------------------------------

    plt.plot(num_tasks_list_fifo, avg_results_fifo, marker='o', label='FIFO Scheduler')
    plt.plot(num_tasks_list_task_estimator, avg_results_task_estimator, marker='o', label='Task Estimator Scheduler')
    plt.plot(num_tasks_list_task_estimator_homo, avg_results_task_estimator_homo, marker='o', label='Task Estimator Heterogeneus Scheduler')
    plt.plot(num_tasks_list_thruput, avg_results_thruput, marker='o', label='Thurput Scheduler')
    plt.plot(num_tasks_list_mtat, avg_results_mtat, marker='o', label='mTAT')
    plt.plot(num_tasks_list_optimal, avg_results_optimal, marker='o', label='Optimal')


  #  plt.plot(num_tasks_list_simple, avg_results_simple, marker='o', label='Simple loop')

    plt.title('Average TAT vs Number of Tasks')
    plt.xlabel('Number of Tasks')
    plt.ylabel('Average TAT Result')
    plt.legend()
    plt.grid(True)
    plt.show()
