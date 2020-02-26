# python3

#from time import time
from heapq import heappush, heappop, heapify
from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [(0, i) for i in range(n_workers)]
    heapify(next_free_time)
    for job in jobs:
        next_time, next_worker = heappop(next_free_time)
        result.append(AssignedJob(next_worker, next_time))
        next_time += job
        heappush(next_free_time, (next_time, next_worker))

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs
    #t1 = time()
    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)
    #t2 = time()
    #print("Time it took was %f" % (t2 - t1))


if __name__ == "__main__":
    main()
