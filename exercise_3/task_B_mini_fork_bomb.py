import multiprocessing as mp
import time
import os

def worker():
    print(f"Child PID {os.getpid()} running...")
    time.sleep(5)

if __name__ == "__main__":
    print("Starting mini fork bomb...")
    children = []

    # Spawn only 8 processes (safe)
    for _ in range(8):
        p = mp.Process(target=worker)
        p.start()
        children.append(p)
        time.sleep(0.2)  # Slow enough for students to observe

    for p in children:
        p.join()

    print("All processes finished.")
