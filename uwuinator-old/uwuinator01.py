import time
import uuid
import subprocess
import os
# from uwu_setup import setup
import shutil

def get_storage(path: str="C:\\"):
    # Get the storage amount left in the external drive.

    usage = shutil.disk_usage(path)
    return usage[2]/1000

def copy(path: str) -> None:
    # Tested with five trials and averaged to 1.71 seconds per 10 files.
    # Simply creates a file and writes the text from uwus.txt into it.
    uwus = open("uwuinator-old/uwus.txt", "r").read()

    open(f"{path}\\UwU-{uuid.uuid4()}.txt", "w").write(uwus)

def subcopy(path: str, filename: str="UwU") -> None:
    # Tested with five trials and averaged to 1.52 seconds per 10 files.
    # Uses a subprocess call to copy the file.
    subprocess.call(["copy", f"{filename.lower()}s.txt", f"{path}\\{filename}-{uuid.uuid4()}.txt"], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def uwuinator(copy_mode: int, path: str, fill_amt: int=0):
    # The main function for the uwuinator.

    print("Initiating UwUs...")

    x = True
    counter = 0

    startime = time.time()
    t1 = time.time()

    if copy_mode == 0:
        copier = copy

    elif copy_mode == 1:
        copier = subcopy

    minute = 0

    while x:
        try:
            copier(path)
            counter += 1
        except Exception as e:
            print(e)
            x = False

        if time.time() - t1 >= 60:
            minute += 1
            t1 = time.time()
            print(f"{counter} Files created in {minute} {'minute' if minute == 1 else 'minutes'} so far...")
        
        if counter == fill_amt:
            x = False
        
        elif get_storage(path) < 2950:
            x = False

    print(f"UwUinator finished in {time.time() - startime} seconds.")

def owoinator():
    path = os.getcwd()

    print("Initiating UwUs...")

    x = True
    counter = 0

    startime = time.time()
    t1 = time.time()

    minute = 0

    while x:
        try:
            subcopy(path, filename="OwO")
            counter += 1
        except IOError:
            x = False

        if time.time() - t1 >= 60:
            minute += 1
            t1 = time.time()
            print(f"{counter} Files created in {minute} {'minute' if minute == 1 else 'minutes'} so far...")

    print(f"OwOinator finished in {time.time() - startime} seconds.")  

def start():
    print("Welcome to the UwUinator! v.0.1.0")

    path = input("Please enter the path to the folder or drive you want to UwUinate: ")

    if path.lower() == "uwu":
        print("UwU")
        exit()
    
    if path.lower() == "owo":
        print("Activating OwOinator...")
        # setup("OwO")
        owoinator()

    if not os.path.exists(path):
        create = input("That path does not exist. Would you like to create it? (y/n): ")
        if create == "y":
            os.mkdir(path)
        else:
            print("Exiting...")
            exit()

    elif not os.path.isdir(path):
        print("That path is not a directory.")
        exit()
    else:
        path = os.path.dirname(path)

    try:
        amt = int(input("How many files do you want to add to the path? 0 to fill the drive: "))
    except ValueError:
        print("That is not a number.")
        exit()

    try:
        mode = int(input(
"""Now select a mode.
0 for standard method
1 for subprocess method (fastest)
"""))
    except ValueError:
        print("Invalid input.")
        return
    
    if mode not in [0, 1]:
        print("Invalid input.")
        return
    
    uwuinator(mode, path, amt)

class UwUinator01:
    
    def __init__(self, path: str):
        self.path = path
        self.startime = time.time()
        self.t1 = time.time()
        self.minute = 0
        self.counter = 0

    def uwuinator(self):
        x = True
        counter = 0

        while x:
            try:
                with open(f"{self.path}\\UwU-{uuid.uuid4()}.txt", "w") as f:
                    f.write("UwU")
                counter += 1
            except Exception as e:
                print(e)
                x = False

            if time.time() - self.t1 >= 60:
                self.minute += 1
                self.t1 = time.time()
                print(f"{counter} Files created in {self.minute} {'minute' if self.minute == 1 else 'minutes'} so far...")

        print(f"UwUinator finished in {time.time() - self.startime} seconds.")

    @classmethod
    def start(cls):
        print("Welcome to the UwUinator! v.0.1.0")

        path = input("Please enter the path to the folder or drive you want to UwUinate: ")

        if path.lower() == "uwu":
            print("UwU")
            exit()
        
        if path.lower() == "owo":
            print("Activating OwOinator...")
            # setup("OwO")
            owoinator()

        if not os.path.exists(path):
            create = input("That path does not exist. Would you like to create it? (y/n): ")
            if create == "y":
                os.mkdir(path)
            else:
                print("Exiting...")
                exit()

        elif not os.path.isdir(path):
            print("That path is not a directory.")
            exit()
        else:
            path = os.path.dirname(path)

        cls(path).uwuinator()

if __name__ == "__main__":
    start()