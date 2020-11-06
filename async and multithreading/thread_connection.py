import threading
from queue import Queue


def create_event(events, queue):
    for event in events:

        thread_notification = threading.Event()

        print(f"New event {event}")

        queue.put((event, thread_notification))


def consume_event(queue):
    while True:
        event, thread_notification = queue.get()
        print(f"{event} PROCESSED")

        thread_notification.set()

        queue.task_done()


events = [[5, 365, 12346, 74234, 7], [67, 2, 452, 5656, 77, 2]]

queue = Queue()

for event_pull in events:
    thread_event_creator = threading.Thread(target=create_event, args=(event_pull, queue))
    thread_event_creator.start()

thread_consume_event1 = threading.Thread(target=consume_event, args=(queue, ))
thread_consume_event1.start()
thread_consume_event2 = threading.Thread(target=consume_event, args=(queue, ))
thread_consume_event2.start()

queue.join()
print("Finish")