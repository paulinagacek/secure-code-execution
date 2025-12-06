# A Step-by-Step Approach to Designing a Secure Software Testing Environment
This repository is the suplement for a Teaching case witht the same name.

## Requirements
- Docker Engine installed and running
- Python 3.x environment
- Linux or WSL environment
- gVisor installed and configured according to the official instructions\footnote{\url{https://gvisor.dev/docs/user_guide/install/}}.  

## Setup
```
git clone https://github.com/paulinagacek/secure-code-execution.git
cd secure-code-execution
```

## Exercise 1

### Setup
Ensure you have the grading script `exercise_1/vulnerable_grader.py` from the repository. You must also create a dummy configuration file named `database.config` in the same directory to act as the target.

### Step 1: The Malicious Submission
Act as the malicious student. Create a file named `student_exploit.py` in `exercise_1` directory. Write Python code that targets the host's file system to delete the config file (e.g., using the `os` module).

### Step 2: Execution and Analysis
Run the grader wrapper, passing your malicious script as an argument:
```bash
python3 exercise_1/vulnerable_grader.py exercise_1/student_exploit.py
```

Check your directory listing `ls -la`; the `database.config` file should be gone. The server script may crash or report a file not found error, confirming the external impact.


## Exercise 2

### Setup:
Build a container: 
```
docker build -t grader-base exercise_2
```

### Step 1: Execution and Analysis
Run the grader wrapper, passing your malicious script from the exercise 1 as an argument:
```bash
python3 exercise_2/grader_with_basic_isolation.py exercise_1/student_exploit.py
```

Check your directory listing `ls -la`; the `database.config` file should be still present.

## Exercise 3

### Setup
Use the same Docker-based grader environment from **Exercise 2**.  
Open `htop` in one terminal to monitor resource usage, and run the grader commands in a second terminal.

---

### Task A — Memory Balloon

The following script gradually allocates memory in small increments.  
Running it inside the **basic** grader allows students to observe uncontrolled memory growth and how it affects the system.

```shell
python3 exercise_2/grader_with_basic_isolation.py exercise_3/task_A_mini_memory_baloon.py
```

Your goal is to update `exercise_3/memory_safe_grader.py` by adding the appropriate Docker memory-limit flag to prevent this uncontrolled growth.

Then rerun the script:
```shell
python3 exercise_3/memory_safe_grader.py exercise_3/task_A_mini_memory_baloon.py 
```

When the script exceeds the memory quota, the container should be terminated cleanly by the Out-of-Memory (OOM) Killer, ensuring the host remains stable.

### Task B — Mini Fork Bomb

First, run the fork bomb script using the basic grader:

```shell
python3 exercise_2/grader_with_basic_isolation.py exercise_3/task_B_mini_fork_bomb.py
```
Then run it again using your improved memory-safe grader:
```shell
python3 exercise_3/memory_safe_grader.py exercise_3/task_B_mini_fork_bomb.py
```

With the correct limits in place, the container should prevent the script from overwhelming the host with excessive process creation.

## Exercise 4

### Task A — The "Uptime" Leak
Create a script `exercise_4/check_uptime.py` that reads how long the operating system has been running.

Run in a standard container (no gVisor):
```
python3 exercise_4/isolated_grader.py exercise_4/check_uptime.py
```

Students should now repeat the experiment using the gVisor-based sandbox:
```
python3 exercise_4/sandboxed_grader.py exercise_4/check_uptime.py
```

### Task B — Kernel Version Fingerprinting
Create a script `exercise_4/check_kernel.py` which query the kernel version.

First, run in a standard container (no gVisor):
```shell
python3 exercise_4/isolated_grader.py exercise_4/check_kernel.py
```
Then run it again using your improved sandboxed grader:
```shell
python3 exercise_4/sandboxed_grader.py exercise_4/check_kernel.py
```

A regular Docker container exposes the host kernel directly, whereas gVisor intercepts the system call and returns a virtualized, sanitized kernel version.