import time
import shutil
from subprocess import call

def shutiltest():
    uwus = open("uwus.txt", "r").read()
    shutil.copyfile("uwus.txt", "shutiltest.txt")

def listcopy():
    uwus = open("uwus.txt", "r").read()
    with open("uwuslist.txt", "w") as f:
        f.write(uwus)

def subprocesstest():
    call(["copy", "uwus.txt", "uwusubprocesstest.txt"], shell=True)

if __name__ == "__main__":
    t1 = time.time()
    shutiltest()
    print(f"Shutil finished in {time.time() - t1} seconds.")
    t2 = time.time()
    listcopy()
    print(f"List copy finished in {time.time() - t2} seconds.")
    t3 = time.time()
    subprocesstest()
    print(f"Subprocess finished in {time.time() - t3} seconds.")
        