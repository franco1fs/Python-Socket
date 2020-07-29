import queue
import threading

orders = queue.Queue()
has_order = threading.Semaphore(value=0)  # ADDED THIS


def serving_line_or_consumer():
    while has_order.acquire():  # ADDED THIS: Acquire a Semaphore, or sleep until the counter of semaphore is larger than zero
        new_order = orders.get()
        # prepare order from `new_order`
        print("Consuming order")
        orders.task_done()


def order_line_or_producer():
    # Each staff in the serving line produces 200 orders
    for _ in range(10):
        print("producing order")
        orders.put("Order")
        has_order.release() # ADDED THIS: Release the Semaphore, increment the internal counter by 1


# Let's put x staff into the order line
order_line = [threading.Thread(target=order_line_or_producer) for _ in range(1)]

# Let's assign x staff into the serving line
serving_line = [threading.Thread(target=serving_line_or_consumer) for _ in range(1)]

# Put all staff to work
[t.start() for t in order_line]
[t.start() for t in serving_line]

print("Start to work")
# "join" the order, block until all orders are cleared
orders.join()


# "join" the threads, ending all threads
[t.join() for t in order_line]
[t.join() for t in serving_line]

print("Finish to work")
#if __name__== "__main__":
 # main()