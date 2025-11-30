### Setup
Ensure you have the grading script `vulnerable_grader.py` from the repository. You must also create a dummy configuration file named `database.config` in the same directory to act as the target.

### Step 1: The Malicious Submission
Act as the malicious student. Create a file named `student_exploit.py`. Write Python code that targets the host's file system to delete the config file (e.g., using the `os` module).

### Step 2: Execution and Analysis
Run the grader wrapper, passing your malicious script as an argument:
```bash
python3 vulnerable_grader.py student_exploit.py
```

Check your directory listing `ls -la`; the `database.config` file should be gone. The server script may crash or report a file not found error, confirming the external impact.