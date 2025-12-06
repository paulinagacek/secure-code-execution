import time

data = []
print("Starting mini memory balloon...")

try:
    while True:
        data.append("x" * 100_000_000)
        time.sleep(0.1)  # gives students time to watch RAM use
        print("Append", flush=True)
except MemoryError:
    print("MemoryError caught: container limit reached safely.", flush=True)
