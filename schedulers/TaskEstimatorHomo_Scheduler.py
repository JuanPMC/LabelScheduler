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