import subprocess
import sys
import os  

def execute_user_code(code_path):
    return subprocess.run(
        ["python3", code_path],
    )

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Please provide the path to the student solution.")
        print("Usage: python3 your_script.py <student_solution.py>")
        sys.exit(1)

    submission_path = sys.argv[1] 
    execute_user_code(submission_path)

    if os.path.exists("exercise_1/database.config"):
        print(">> ATTACK FAILED: 'database.config' is still present.")
    else:
        print(">> ATTACK SUCCESS: 'database.config' deleted.")