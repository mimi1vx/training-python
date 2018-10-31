import multiprocessing
import math
import sys
import time


class Factorial(multiprocessing.Process):
    def __init__(self, n, queue):
        multiprocessing.Process.__init__(self)
        self.n = n
        self.queue = queue

    def run(self):
        result = 1
        for i in range(1, self.n + 1):
            result *= i
        self.queue.put(result)


if __name__ == "__main__":
    queue = multiprocessing.Queue()
    process = Factorial(int(sys.argv[1]), queue)
    process.start()
    while queue.empty():
        print(".", end="", file=sys.stderr)
        sys.stderr.flush()
        time.sleep(0.2)
    print("Result: {0}".format(queue.get()), file=sys.stderr)
    process.join()
