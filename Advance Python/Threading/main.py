# Definition of Threading in Python

# Threading means running multiple tasks at the same time inside a single process.

# Each thread is a lightweight unit of execution.

# Python provides a threading module to create and manage threads.

# Useful for tasks like downloading files, I/O operations, background jobs, etc.

# import threading
# import time

# # Function to simulate a task
# def print_numbers():
#     for i in range(1, 6):
#         print("Number:", i)
#         time.sleep(1)  # simulate some delay

# def print_letters():
#     for ch in ['A', 'B', 'C', 'D', 'E']:
#         print("Letter:", ch)
#         time.sleep(1)

# # Main program
# if __name__ == "__main__":
#     # Create threads
#     t1 = threading.Thread(target=print_numbers)
#     t2 = threading.Thread(target=print_letters)

#     # Start threads
#     t1.start()
#     t2.start()

#     # Wait until both threads finish
#     t1.join()
#     t2.join()

#     print("✅ Both threads finished execution")
    

#Class based threading

import threading
import time

# Create a thread class by extending threading.Thread
class MyThread(threading.Thread):
    def __init__(self, name):
        super().__init__()   # Call parent class constructor   
        # super().__init__() → tells Python: "Hey, also run the parent class’s constructor so my thread object is fully prepared."
        
        self.name = name

    # Override the run() method (this runs when we call start())
    def run(self):
        print(f"Thread {self.name} started")
        for i in range(1, 4):
            print(f"Thread {self.name} -> Count {i}")
            time.sleep(1)  # simulate work
        print(f"Thread {self.name} finished")

# Main program
if __name__ == "__main__":
    # Create thread objects
    t1 = MyThread("A")
    t2 = MyThread("B")

    # Start threads (this internally calls run())
    t1.start()
    t2.start()

    # Wait for both threads to complete
    t1.join()
    t2.join()

    print("✅ All threads completed")
    
    
