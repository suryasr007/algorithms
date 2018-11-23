"""
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""
import time

def schedule(f, n):
    time.sleep(n/1000)
    return f()

if __name__ == "__main__":
    print(schedule(lambda: "Hi After 2 seconds", 2000))