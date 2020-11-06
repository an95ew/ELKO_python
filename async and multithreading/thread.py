from threading import Thread
import random
import time


class Resource:
    def __init__(self):
        self.value = 1


class NumberPrinter(Thread):

    def __init__(self, thread_id, resource):
        Thread.__init__(self)
        self.thread_id = thread_id
        self.resource = resource

    def run(self):
        number = random.randint(1, 3)
        time.sleep(number)
        self.resource.value +=1
        print(f"thread {self.name} is running with number - {number}, value = {self.resource.value}")


# RUN FEW THREADS
resource = Resource()

for i in range(20):
    thread = NumberPrinter(i, resource)
    thread.start()
    # thread.join()

print(resource.value)