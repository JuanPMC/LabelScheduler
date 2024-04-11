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