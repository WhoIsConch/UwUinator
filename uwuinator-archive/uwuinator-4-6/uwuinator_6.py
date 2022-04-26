import time
import uuid
import os
import threading

"""
UwUinator 6.0 copies an image file multiple times to a specified path with threading.

PERSONAL TESTS:
- 4gb Memorex drive:
    - Real Space: 3.6gb

    - Time to fill: 15.97 Minutes
    - Average speed: 4.2 MB/s
    - Total files copied: 454
"""

class UwUinator():
    def __init__(self, path: str = "E:"):
        self.path = path
        self.startime = time.time()
        self.t1 = time.time()
        self.minute = 0
        self.counter = 0
        self.file = os.getcwd() + "\\uwuinator\\img.jpg"
        self.speeds = []
        self.main_thread: threading.Thread

        with open(self.file, "rb") as f:
            self.data = f.read()
    
    @property
    def size(self):
        return os.path.getsize(self.file)
    
    @property
    def filled(self):
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

    def show_stats(self, thread_count: int):
        print(
            f"Approximately {self.minute} minutes have passed so far ({round((self.t1 - self.startime)/60, 2)} minutes).\n"
            "Stats:\n"
            f"  Files Written: {self.counter}\n"
            f"  Approximate Speed: {self._get_mbps(self.counter, self.minute)} MB/s\n"
            f"  Amount of drive filled: {self.filled}\n"
            f"  Current thread count: {thread_count}"
            )

    def uwuinator(self):
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
                    f"  Amount of drive filled: {self.filled}\n"
                    f"  Current thread count: {threading.active_count()}\n"
                    f"  Current thread: {threading.current_thread().name}\n"
                    )
                
                self.speeds.append(self._get_mbps(self.counter, self.minute))

        print(f"UwUinator finished in {round(time.time() - self.startime)} seconds ({round((time.time() - self.startime)/60, 2)} minutes).")
        print(f"Files created: {self.counter}")
        print(f"Average speed: {round(sum(self.speeds) / len(self.speeds), 2)} MB/s")
        print(f"Amount of drive filled: {self.filled}")

    @classmethod
    def start(cls):
        print("Welcome to the UwUinator! v.0.6.0")

        path = input("Please enter the path to the folder or drive you want to UwUinate (empty for C:\): ")

        if path == "":
            path = "C:\\"

        elif not os.path.exists(path):
            print("Invalid path.")
            exit()
        
        print("UwUinating...")

        uwu = cls(path)

        for i in range(5):
            t = threading.Thread(target=uwu.uwuinator)
            t.start()

if __name__ == "__main__":
    UwUinator.start()