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
        
    def compute_duration(self,tasks):
        total_duration = 0
        for task in tasks:
            total_duration += self.computeTime(task)
        return total_duration
