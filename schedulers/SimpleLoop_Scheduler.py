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
