import time
import uuid
import subprocess
import os

"""
The UwUinator is a tool that can be used to generate a bunch of UwU files in a specified path, usually an external drive.
UwUinator 0.2.0 uses the `subprocess` `check_call` method to copy the `uwus.txt` file to the specified path.
"""

class UwUinator():
    def __init__(self, path: str = "C:\\", file: str = "uwus.txt"):
        self.path = path
        self.startime = time.time()
        self.t1 = time.time()
        self.minute = 0
        self.counter = 0
        self.file = file
        self.speeds = []
    
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

    def uwuinator(self):
        self.counter = 0

        while True:
            try:
                subprocess.check_call(["copy", f"uwus.txt", f"\"E:\\UwU-{uuid.uuid4()}.txt\""], shell=True, stdout=subprocess.DEVNULL)
            except subprocess.CalledProcessError as e:
                print(e)
                print(e.output)
                print(e.returncode)
                print(e.args)
                try:
                    with open(f"E:\\UwU-{uuid.uuid4()}.txt", "w") as f:
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
        print("Welcome to the UwUinator! v.0.2.0")

        path = input("Please enter the path to the folder or drive you want to UwUinate (empty for C:\): ")

        if path == "":
            path = "C:\\"

        elif not os.path.exists(path):
            print("Invalid path.")
            exit()
        
        file = input("Please enter the path to the file you want to use (empty for default UwUs): ")

        if file == "":
            file = "uwus.txt"

        elif not os.path.exists(file):
            print("Invalid file.")
            exit()
        
        print("UwUinating...")
        cls(path, file).uwuinator()   

if __name__ == "__main__":
    UwUinator.start()