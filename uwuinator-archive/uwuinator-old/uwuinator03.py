import time
import uuid

class UwUinator03():
    def __init__(self, path: str):
        self.path = path
        self.startime = time.time()
        self.t1 = time.time()
        self.minute = 0
        self.counter = 0
        self.speeds = []

    def start(self):
        print("Starting UwUinator v.0.3.0...")
        with open(f"{self.path}\\UwU-{uuid.uuid4()}.txt", "w") as f:
            try:
                while True:
                    f.write("UwU")
                    self.counter += 1

                    if self.counter % 1000000 == 0:
                        print(f"{self.counter} iterations completed in {time.time() - self.startime} so far...")
            except:
                print(f"Done in {time.time() - self.t1} seconds.")
         