import time
import os

def setup() -> None:
    with open("uwus_old.txt", "r") as f:
        uwus = f.read()
    
    t1 = time.time()
    with open("uwus.txt", "w") as f:
        for i in range(5):
            f.write(uwus)
            print(i)
            print(time.time() - t1)
            t1 = time.time()
    
    print("Complete.")

if __name__ == "__main__":
    setup()
        