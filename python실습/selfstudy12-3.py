import threading
import time

class SumCalculator :
    
    def __init__(self, limit):
        self.limit = limit
        self.total_sum = 0 

    
    def calculate_sum(self):
        current_sum = 0
        for i in range(1, self.limit + 1):
            current_sum += i
        self.total_sum = current_sum 


calc1 = SumCalculator(1000)
calc2 = SumCalculator(100000)
calc3 = SumCalculator(100000000)

th1 = threading.Thread(target = calc1.calculate_sum)
th2 = threading.Thread(target = calc2.calculate_sum)
th3 = threading.Thread(target = calc3.calculate_sum)

th1.start()
th2.start()
th3.start()

th1.join()
th2.join()
th3.join()

print(f"1+2+3+...+1000 = {calc1.total_sum}")
print(f"1+2+3+...+100000 = {calc2.total_sum}")
print(f"1+2+3+...+100000000 = {calc3.total_sum}")