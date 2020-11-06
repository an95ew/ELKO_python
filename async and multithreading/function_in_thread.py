import threading


resource = 0
lock = threading.Lock()

def update(new_value):
    global resource

    with lock:
        resource += new_value

    print(resource)


for i in range(10):
    thread = threading.Thread(target=update, args=(100, ))
    thread.start()
