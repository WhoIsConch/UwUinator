import os
import time
import subprocess
import uuid

def pathtest(path):
    path = os.path.dirname(path)
    print(path)

def copytest(path):
    subprocess.call(["copy", f"uwus.txt", f"{path}\\UwU-{uuid.uuid4()}.txt"], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def copytest2(path):
    proc = subprocess.Popen(["copy", f"uwus.txt", f"{path}\\UwU-{uuid.uuid4()}.txt"], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    proc.wait()

def copytest3(path):
    subprocess.check_call(["copy", f"uwus.txt", f"{path}\\UwU-{uuid.uuid4()}.txt"], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if __name__ == "__main__":
    t1 = time.time()
    copytest("E:\\")
    print(f"Done in {time.time() - t1} seconds.")
    t2 = time.time()
    copytest2("E:\\")
    print(f"Done in {time.time() - t2} seconds.")
    t3 = time.time()
    copytest3("E:\\")
    print(f"Done in {time.time() - t3} seconds.")