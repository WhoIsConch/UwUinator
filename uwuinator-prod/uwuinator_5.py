import time
import uuid
import os
import asyncio
import math

"""
UwUinator 5.0 copies the same image multiple times to a specified path using async I/O.

PERSONAL TESTS:

- 4gb Memorex drive:
    - Real Space: 3.6gb

    - Time to fill: 15.36 Minutes
    - Average Speed: 4.25 MB/s
    - Total files copied: 454
    - Amount Filled: 3.6gb

- Phoenix 128gb Samsung Flash Drive:
    - Real Space: 119gb

    - TEST 1:
        - Time to fill: Not filled. Test for 30 Gigabytes.
        - Average speed: 51.12 MB/s
        - Total files copied: 5150
        - Amount Filled: 32.74gb

- Louis 4GB DVD-RW:
    - Real Space: 4.25gb

    - TEST 1:
        - Time to fill: 28.97 Minutes
        - Average speed: 2.56 MB/s
        - Total files copied: 668
        - Amount Filled: 4.25gb

"""

class UwUinator:
    def __init__(self, path: str = "E:", file: str = os.getcwd() + "\\img.jpg") -> None:
        self.path = path
        self.startime = time.time()
        self.t1 = time.time()
        self.minute = 0
        self.counter = 0
        self.file = file
        self.file_size = os.path.getsize(self.file)
        self.speeds = []

        with open(self.file, "rb") as f:
            self.data = f.read()
    
    @property
    def size(self) -> int:
        return self.file_size
    
    def get_filled(self) -> str:
        units = ('B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB')

        power = int(math.log(self.size * self.counter, 1024))

        return f"{self.size * self.counter / (1024 ** power):.2f} {units[power]}"

    def _get_mbps(self, file_amt: int, time: int) -> float:
        return round((file_amt * ((self.size / 1024) / 1024)) / (time * 60), 2)

    async def copy(self) -> bool:
        try:
            with open(f"{self.path}\\UwU-{uuid.uuid4()}.jpg", "wb") as f:
                f.write(self.data)
            return True
        except:
            return False

    async def uwuinator(self) -> None:
        self.counter = 0

        while True:

            status = await self.copy()
            
            if not status:
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

        print(f"UwUinator finished in {round(time.time() - self.startime)} seconds ({round((time.time() - self.startime)/60, 2)} minutes).")
        print(f"Files created: {self.counter}")
        print(f"Average speed: {round(sum(self.speeds) / len(self.speeds), 2)} MB/s")
        print(f"Amount of drive filled: {self.get_filled()}")

    @classmethod
    async def start(cls) -> None:
        print("Welcome to the UwUinator! v.1.5.1")

        while True:
            path = input("Please enter the path to the folder or drive you want to UwUinate (empty for C:\): ")

            if path == "":
                path = "C:"
                break

            elif not os.path.exists(path):
                print("Invalid path.")
                continue
            else:
                break
        
        file = os.path.exists(os.getcwd() + "\\img.jpg")

        if not file:
            while True:
                file = input("Image file not found. Enter the path to the image file now: ")

                if not os.path.exists(file):
                    continue
                else:
                    break

        uwu = cls(path, file) 
        
        print("UwUinating...")
        await uwu.uwuinator()

        

if __name__ == "__main__":
    asyncio.run(UwUinator.start())