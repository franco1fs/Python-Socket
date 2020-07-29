import threading
import time
import random

condition = threading.Condition()
queue = []

class ConsumerThread(threading.Thread):
    def run(self):
        global queue
        time_elapsed = 0.0
        while True:
            if time_elapsed > 0.5:
                return
            condition.acquire()
            if not queue:
                print ("Nothing in queue, consumer will wait.")
                condition.wait()
                print ("Producer added something to queue - consumer will stop waiting.")
            num = queue.pop(0)
            print ("Consumed", num)
            condition.release()
            time.sleep(0.1)
            time_elapsed += 0.1
            
class ProducerThread(threading.Thread):
    def run(self):
        produce_number = 1
        global queue
        time_elapsed = 0.0
        while True:
            if time_elapsed > 0.5:
                return
            condition.acquire()
            queue.append(produce_number)
            print ("Produced", produce_number)
            condition.notify()
            condition.release()
            produce_number += 1
            time.sleep(0.1)
            time_elapsed += 0.1
            
ProducerThread().start()

ConsumerThread().start()
