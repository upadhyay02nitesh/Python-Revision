# from threading import Thread, current_thread
# class Flight:
#     def __init__(self, available_seat, flight_number):
#         self.available_seat = available_seat
#         self.flight_number = flight_number

#     def reserve_seat(self, need_seat):
#         name=current_thread().name
#         if self.available_seat >= need_seat:
#             print(f"Reserving {name}  to {need_seat} seats on flight {self.flight_number}")
#             self.available_seat -= need_seat
#         else:
#             print(f"No available seats on flight {self.flight_number}")
            

# f=Flight(1,"AI202")
# t1=Thread(target=f.reserve_seat,args=(1,),name="Rahul")
# t2=Thread(target=f.reserve_seat,args=(1,),name="Sita")
# t1.start()
# t2.start()



# 🔎 Why Race Condition Occurs Here?
# A race condition happens when multiple threads access and modify the same
# shared resource (here, available_seat) at the same time without proper synchronization.

# Timeline of What Might Happen:
# Rahul thread checks → available_seat == 1 ✅

# Before Rahul subtracts, Python switches context to Sita thread.

# Sita also checks → still sees available_seat == 1 ✅

# Both think seat is available → both reserve.

# Now both threads subtract 1 → seat count becomes -1 (or double booking).

# 👉 This leads to inconsistent or incorrect results.



# self.lock.acquire() → thread takes ownership of the lock.

# If another thread tries to acquire it while it’s already held → 
# it must wait until the lock is released.




# from threading import Thread, current_thread,Lock
# class Flight:
#     def __init__(self, available_seat, flight_number):
#         self.available_seat = available_seat
#         self.flight_number = flight_number
#         self.lock = Lock()

#     def reserve_seat(self, need_seat):
#         name=current_thread().name
#         self.lock.acquire()
#         if self.available_seat >= need_seat:
#             print(f"Reserving {name}  to {need_seat} seats on flight {self.flight_number}")
#             self.available_seat -= need_seat
#         else:
#             print(f"No available seats on flight {self.flight_number}")
#         self.lock.release()
            

# f=Flight(1,"AI202")
# t1=Thread(target=f.reserve_seat,args=(1,),name="Rahul")
# t2=Thread(target=f.reserve_seat,args=(1,),name="Sita")
# t1.start()
# t2.start()




# from threading import Thread, current_thread,Lock,RLock
# class Flight:
#     def __init__(self, available_seat, flight_number):
#         self.available_seat = available_seat
#         self.flight_number = flight_number
#         self.lock = RLock()

#     def reserve_seat(self, need_seat):
#         name=current_thread().name
#         self.lock.acquire()
#         print(self.lock)
#         if self.available_seat >= need_seat:
#             print(f"Reserving {name}  to {need_seat} seats on flight {self.flight_number}")
#             self.available_seat -= need_seat
#         else:
#             print(f"No available seats on flight {self.flight_number}")
#         self.lock.release()
            

# f=Flight(1,"AI202")
# t1=Thread(target=f.reserve_seat,args=(1,),name="Rahul")
# t2=Thread(target=f.reserve_seat,args=(1,),name="Sita")
# t1.start()
# t2.start()


# 1. Lock (threading.Lock)

# A basic lock that can be acquired only once.

# If the same thread tries to acquire it again without releasing → it will block forever (deadlock).

# Very lightweight, so use it when you don’t need nested locking.


# 🔹 2. RLock (threading.RLock)

# Reentrant Lock = a lock that the same thread can acquire multiple times.

# Keeps a count of how many times it’s acquired.

# The thread must release it the same number of times before another thread can acquire it.

# Useful when a function that needs a lock calls another function that also needs
# the same lock.



# from threading import Thread, current_thread,Lock,RLock
# class Flight:
#     def __init__(self, available_seat, flight_number):
#         self.available_seat = available_seat
#         self.flight_number = flight_number
#         self.lock = RLock()

#     def reserve_seat(self, need_seat):
#         name=current_thread().name
#         self.lock.acquire()
#         print(self.lock)
#         if self.available_seat >= need_seat:
#             print(f"Reserving {name}  to {need_seat} seats on flight {self.flight_number}")
#             self.available_seat -= need_seat
#         else:
#             print(f"No available seats on flight {self.flight_number}")
#         self.lock.release()
            

# f=Flight(1,"AI202")
# t1=Thread(target=f.reserve_seat,args=(1,),name="Rahul")
# t2=Thread(target=f.reserve_seat,args=(1,),name="Sita")
# t1.start()
# t2.start()


from threading import RLock

class Flight:
    def __init__(self, seats):
        self.seats = seats
        self.lock = RLock()

    def book_ticket(self, name):
        with self.lock:
            print(f"{name} booking started...")
            self.update_database(name)  # nested call

    def update_database(self, name):
        with self.lock:  # nested lock
            print(f"Updating database for {name}")
            self.seats -= 1
            print(f"Seats left: {self.seats}")

f = Flight(2)
f.book_ticket("Rahul")
f.book_ticket("Sita")


# Rahul booking started...
# Updating database for Rahul
# Seats left: 1
# Sita booking started...
# Updating database for Sita
# Seats left: 0

# BookTicket and UpdateDatabase both use the same RLock (self.lock).

# When Rahul calls BookTicket:

# He acquires the lock the first time in BookTicket.

# Inside BookTicket, UpdateDatabase tries to acquire the same lock again → allowed because it’s reentrant.

# Now the lock counter = 2.

# After UpdateDatabase finishes → counter = 1.

# After BookTicket finishes → counter = 0 → lock is fully released.

# ✅ Only after Rahul finishes both methods, Sita can acquire the lock and access the flight booking.

# This prevents race conditions and ensures nested calls by the same thread work safely.



# 🔹 1. When Multithreading is Important

# Multithreading is useful whenever you want to perform multiple tasks concurrently without waiting for each to finish sequentially.

# Real Use Cases

# Web Servers / APIs

# Multiple users send requests at the same time.

# Each request is handled by a separate thread to avoid blocking.

# Example: Flask/Django handling hundreds of simultaneous users.

# File Downloads / Uploads

# Downloading multiple files concurrently saves time.

# Example: A torrent client downloading pieces of a file in parallel.

# GUI Applications

# To prevent freezing of the interface while performing a long task.

# Example: Loading images in the background in a desktop app.

# I/O Bound Operations

# Database calls, API calls, reading/writing files.

# Threads let CPU continue other tasks while waiting for I/O.

# 🔹 2. Why Race Condition is Important

# Race conditions occur when multiple threads access and modify the same shared 
# resource at the same time.

# Real Use Cases

# Banking Systems

# Multiple users trying to withdraw from the same account.

# Without proper locking, two withdrawals may reduce balance incorrectly → loss of money.

# Flight or Ticket Booking

# Multiple users booking the last seat on a flight.

# Without locks, two people may get booked for the same seat → double booking.

# Inventory Management / E-commerce

# Multiple threads updating product stock.

# Without synchronization, stock can go negative or orders can oversell.

# Shared Counters / Logs

# Multiple threads incrementing counters or writing logs.

# Without protection, the counter or log can be corrupted.

# 🔹 Key Takeaways

# Use multithreading → when tasks can run concurrently to improve speed or responsiveness.

# Handle race conditions → when threads share resources to ensure data consistency 
# and correctness.

# Tools: Lock, RLock, Semaphore in Python.



# 💡 Simple rule of thumb:

# Multithreading → improves performance or responsiveness.

# Race condition management → ensures accuracy when threads share data.

# ✅ Simpler Version of the Sentence

# Threads are useful for tasks that involve calculations or waiting for
# I/O, but they use more memory and r
# equire locks when sharing data between threads.