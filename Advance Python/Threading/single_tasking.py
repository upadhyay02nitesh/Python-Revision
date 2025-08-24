from threading import Thread

from time import sleep

class MyExam:
    def solve_question(self):
       self.q1()
       self.q2()
       self.q3()
    
    
    def q1(self):
        print("Solving Question 1")
        sleep(2)  # Simulate time taken to solve the question
        print("Finished solving Question 1")    
    
    def q2(self):
        print("Solving Question 2")
        sleep(2)  # Simulate time taken to solve the question
        print("Finished solving Question 2")

    def q3(self):
        print("Solving Question 3")
        sleep(2)  # Simulate time taken to solve the question
        print("Finished solving Question 3")
m=MyExam()
t=Thread(target=m.solve_question)
t.start()