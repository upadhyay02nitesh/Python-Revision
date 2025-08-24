# asyncio allows multiple tasks to run concurrently, making programs faster when waiting 
# for things like I/O or network calls, without using threads.

# 1️⃣ async

# async is used to define a coroutine (a special kind of function that can pause and resume).

# Normal function: runs from start to end, blocking everything else.

# Async function: can pause at await, letting other tasks run in the meantime.

# 2️⃣ await

# await is used inside an async function.

# It tells Python:

# “Pause here until this task finishes, but don’t block other tasks from running.”

# You cannot use await in a normal function. Only inside async def.



import asyncio


async def func1():
    print("Function 1 started..")
    await asyncio.sleep(2)
    print("Function 1 Ended")


async def func2():
    print("Function 2 started..")
    await asyncio.sleep(3)
    print("Function 2 Ended")


async def func3():
    print("Function 3 started..")
    await asyncio.sleep(1)
    print("Function 3 Ended")


async def main():
    L = await asyncio.gather(
        func1(),
        func2(),
        func3(),
    )
    print("Main Ended..")


asyncio.run(main())

# They pause at await asyncio.sleep():

# func1 → 2 sec

# func2 → 3 sec

# func3 → 1 sec

# Which finishes first?

# func3 → only 1 second → prints "Function 3 Ended"

# Next finish?

# func1 → 2 seconds → prints "Function 1 Ended"

# Last finish?

# func2 → 3 seconds → prints "Function 2 Ended"



# ✅ Summary

# Order of ending depends on await sleep duration,
# not the order you write the functions.

# Shortest sleep → ends first

# Longest sleep → ends last

# 3️⃣ Visual Flow (Simple Timeline)

#                     Start asyncio.run(main())
#                             │
#                             ▼
#                     main() starts
#                             │
#                     gather(task1, task2, task3)
#                             │
#                     ┌───── Tasks start concurrently ─────┐
#                     │ task1: sleep 2s                   │
#                     │ task2: sleep 3s                   │
#                     │ task3: sleep 1s                   │
#                     └───────────────────────────────────┘
#                             │
#                     task3 finishes after 1s → prints
#                     task1 finishes after 2s → prints
#                     task2 finishes after 3s → prints
#                             │
#                         main() prints "All done"
#                             │
#                     End of asyncio.run()


# ✅ Key Idea:

# async → defines a coroutine

# await → pause here but don’t block others

# asyncio → manages async tasks

# asyncio.run() → starts everything and waits for all to finish