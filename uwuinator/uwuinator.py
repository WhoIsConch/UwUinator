import time
import uuid
import os
import asyncio
import math
import shutil

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
    def __init__(self, path: str, file: str, amount: int | bool) -> None:
        self.path = path
        self.file = file
        self.file_size = os.path.getsize(self.file)
        self.amt = amount
        self.startime = time.time()
        self.t1 = time.time()
        self.minute = 0
        self.counter = 0
        self.speeds = []
        self.path_space = shutil.disk_usage(self.path).free

        with open(self.file, "rb") as f:
            self.data = f.read()
    
    @property
    def size(self) -> int:
        return self.file_size
    
    def get_filled(self) -> str:
        '''
        Gets the total space filled by the UwUinator.
        '''
        units = ('B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB')

        if self.counter == 0:
            return "0 MB"

        power = int(math.log(self.size * self.counter, 1024))

        return f"{self.size * self.counter / (1024 ** power):.2f} {units[power]}"

    def _get_mbps(self, file_amt: int, time: int) -> float:
        '''
        Gets the average write speed of the UwUinator.
        '''
        return round((file_amt * ((self.size / 1024) / 1024)) / (time * 60), 2)

    async def copy(self) -> bool:
        '''
        Copies the file to the specified path.
        '''
        path = self.path + "\\UwU-" + str(uuid.uuid4()) + "." + str(self.file.split('\\')[-1].split('.')[-1])
        try:
            with open(path, "wb") as f:
                f.write(self.data)
            return True
        except:
            return False

    async def uwuinator(self) -> None:
        '''
        The main function of the UwUinator.
        '''
        self.counter = 0

        while True:
            filled = self.get_filled()

            if self.amt:
                if filled.endswith('MiB'):
                    if self.amt <= float(filled.split(' ')[0]):
                        break
                
                elif filled.endswith('GiB'):
                    if self.amt * 1024 <= float(filled.split(' ')[0]):
                        break
                
                elif filled.endswith('TiB'):
                    if self.amt * 1024 * 1024 <= float(filled.split(' ')[0]):
                        break

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

                self.path_space = shutil.disk_usage(self.path).free

                time_taken = time.time() - self.startime

                time_left = round(((self.path_space / (self.size * self.counter)) * time_taken)/60, 2)
                

                curr_speed = self._get_mbps(self.counter, self.minute)
                self.speeds.append(curr_speed)

                print(
                    f"Approximately {self.minute} minutes have passed so far ({round((self.t1 - self.startime)/60, 2)} minutes).\n"
                    "Stats:\n"
                    f"  Files Written: {self.counter}\n"
                    f"  Approximate Speed: {self._get_mbps(self.counter, self.minute)} MB/s\n"
                    f"  Amount of drive filled: {self.get_filled()}\n"
                    f"  Time until complete: approx. {time_left} Minutes\n"
                    )

        print(f"UwUinator finished in {round(time.time() - self.startime)} seconds ({round((time.time() - self.startime)/60, 2)} minutes).")
        print(f"Files created: {self.counter}")
        try:
            print(f"Average speed: {round(sum(self.speeds) / len(self.speeds), 2)} MB/s")
        except ZeroDivisionError:
            print("Average speed: N/A")
        print(f"Amount of drive filled by UwUinator: {self.get_filled()}")

    @classmethod
    async def start(cls, path: str, amount: int | bool, file: str=None, ) -> None:
        '''
        Starts the UwUinator.
        '''
        print("Welcome to the UwUinator! v.1.5.4")
        
        if not file:
            file = os.path.join(os.path.dirname(__file__), "img.jpg")

            file_exists = os.path.exists(file)

            # Check if the local file exists, and ask the user to provide that path to it if it does not.
            if not file_exists:
                while True:
                    fp = input("Image file not found. Enter the path to the image file now: ")

                    if not os.path.exists(fp):
                        continue
                    else:
                        break

        uwu = cls(path, file, amount) 
        
        print("UwUinating...")
        await uwu.uwuinator()

        

if __name__ == "__main__":
    asyncio.run(UwUinator.start("E:", False))