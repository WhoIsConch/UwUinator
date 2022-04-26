import time
import uuid
import os
import py7zr

"""
UwUinator 7.0 extracts UwU text files to a directory.

PERSONAL TESTS:
- 4gb Memorex drive:
    - Real Space: 3.6gb

    - Time to fill:  Minutes
    - Average speed:  MB/s
    - Total files copied: 
"""

class UwUinator():
    def __init__(self, path: str = "E:"):
        self.path = path
        self.startime = time.time()
        self.t1 = time.time()
        self.minute = 0
        self.counter = 0
        self.file = "uwuinator-7/homework.7z"
        self.speeds = []
        self.archive = py7zr.SevenZipFile("uwuinator-7/homework.7z", 'r') 
    
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
        with self.archive as archive:
            archive.extractall(path=self.path)
        
        print(f"Extracted {self.counter} archive(s).")

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
                    f"  Amount of drive filled: {self.filled}\n"
                    )
                
                self.speeds.append(self._get_mbps(self.counter, self.minute))

        print(f"UwUinator finished in {round(time.time() - self.startime)} seconds ({round((time.time() - self.startime)/60, 2)} minutes).")
        print(f"Files created: {self.counter}")
        print(f"Average speed: {round(sum(self.speeds) / len(self.speeds), 2)} MB/s")
        print(f"Amount of drive filled: {self.filled}")

    @classmethod
    def start(cls):
        print("Welcome to the UwUinator! v.0.4.0")

        path = input("Please enter the path to the folder or drive you want to UwUinate (empty for C:\): ")

        if path == "":
            path = "C:\\"

        elif not os.path.exists(path):
            print("Invalid path.")
            exit()
        
        print("UwUinating...")
        cls(path).uwuinator()   

if __name__ == "__main__":
    UwUinator.start()