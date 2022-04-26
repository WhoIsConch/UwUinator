import time
import uuid
import os

"""
UwUinator 4.0 copies an image file multiple times to a specified path.

PERSONAL TESTS:
- 4gb Memorex Flash Drive:
    - Real Space: 3.6gb

    - TEST 1:
        - Time to fill: 15.71 Minutes
        - Average speed: 4.08 MB/s
        - Total files copied: 454
        - Amount Filled: 3.6gb
    
    - TEST 2:
        Test 2 has a different file size than test 1, at 6.666mb instead of 8.312mb.
        - Time to fill: 15.71 Minutes
        - Average speed: 4.11 MB/s
        - Total files copied: 556
        - Amount Filled: 3.6gb

- Phoenix 128gb Samsung Flash Drive:
    - Real Space: 119gb

    - TEST 1:
        - Time to fill: Not filled. Test for 30 Gigabytes.
        - Average speed: 52.27 MB/s
        - Total files copied: 4733
        - Amount Filled: 30.09gb
"""

class UwUinator:
    def __init__(self, path: str = "E:"):
        self.path = path
        self.startime = time.time()
        self.t1 = time.time()
        self.minute = 0
        self.counter = 0
        self.file = "uwuinator/img.jpg"
        self.size = os.path.getsize(self.file)
        self.speeds = []

        with open(self.file, "rb") as f:
            self.data = f.read()
    
    @property
    def size(self):
        return self.size
    
    def get_filled(self):
        size = round(self.counter * ((self.size / 1024) / 1024), 2)
        
        if size >= 1024:
            return f"{round(size / 1024, 2)} GB"
        else:
            return f"{size} MB"

    def _get_mbps(self, file_amt: int, time: int):
        size = (self.size / 1024) / 1024

        return round((file_amt * size) / (time * 60), 2)

    def copy(self):
        with open(f"{self.path}\\UwU-{uuid.uuid4()}.jpg", "wb") as f:
            f.write(self.data)

    def uwuinator(self):
        self.counter = 0

        while True:
            try:
                self.copy()
            except Exception as e:
                print(e)
                try:
                    with open(f"{self.path}\\UwU-{uuid.uuid4()}.txt", "w") as f:
                        while True:
                            f.write("UwU")
                except:
                    break

            self.counter += 1

            if time.time() - self.t1 >= 60:
                self.minute += 1
                self.t1 = time.time()
                print(
                    f"Approximately {self.minute} minutes have passed so far ({round((self.t1 - self.startime)/60, 2)} minutes).\n"
                    "Stats:\n"
                    f"  Files Written: {self.counter}\n"
                    f"  Approximate Speed: {self._get_mbps(self.counter, self.minute)} MB/s\n"
                    f"  Amount of drive filled: {self.get_filled()}\n"
                    )
                
                self.speeds.append(self._get_mbps(self.counter, self.minute))

                if float(self.get_filled().replace('GB', '').strip()) >= 30:
                    break

        print(f"UwUinator finished in {round(time.time() - self.startime)} seconds ({round((time.time() - self.startime)/60, 2)} minutes).")
        print(f"Files created: {self.counter}")
        print(f"Average speed: {round(sum(self.speeds) / len(self.speeds), 2)} MB/s")
        print(f"Amount of drive filled: {self.get_filled()}")

    @classmethod
    def start(cls):
        print("Welcome to the UwUinator! v.0.4.0")

        path = input("Please enter the path to the folder or drive you want to UwUinate (empty for E:): ")

        if path == "":
            path = "C:\\"

        elif not os.path.exists(path):
            print("Invalid path.")
            exit()
        
        print("UwUinating...")
        cls(path).uwuinator()   

if __name__ == "__main__":
    UwUinator.start()