import subprocess
import sys
import os # Import the os module

def execute_in_container(host_path):
    absolute_path = os.path.abspath(host_path)
    print(f"Mounting {host_path} as {absolute_path}...")

    return subprocess.run(
        ["docker", "run", "--rm", 
         "-v", f"{absolute_path}:/app/script.py", 
         "grader-base", "python3", "/app/script.py"],
    )

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Please provide the path to the student solution.")
        print("Usage: python3 grader_with_basic_isolation.py <student_solution.py>")
        sys.exit(1)

    submission_path = sys.argv[1] 
    
    execute_in_container(submission_path)

    if os.path.exists("exercise_2/database.config"):
        print(">> ATTACK FAILED: 'database.config' is still present.")
    else:
        print(">> ATTACK SUCCESS: 'database.config' deleted.")