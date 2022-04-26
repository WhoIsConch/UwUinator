import time
import os

def setup(string: str) -> None:
    if os.path.exists(os.getcwd() + "\\" + string.lower() + "s.txt"):
        return

    time1 = time.time()

    print("Starting...")

    with open(f"{string.lower()}s.txt", "a") as f:
        counter = 0
        while True:
            f.write(string)
            counter += 1
            if counter % 100 == 0:
                f.write("\n")
            if counter == 1000000:
                break

    print(f"Finished in {time.time() - time1}")
        