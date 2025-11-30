import subprocess
import sys  

def grade_submission(script_path):
    print(f"[Server] Grading {script_path}...")
    subprocess.run(["python3", script_path])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Please provide the path to the student solution.")
        print("Usage: python your_script.py <student_solution.py>")
        sys.exit(1)

    submission_path = sys.argv[1] 
    grade_submission(submission_path)