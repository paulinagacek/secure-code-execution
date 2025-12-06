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