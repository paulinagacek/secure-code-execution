import subprocess
import sys
import os


def execute_in_container(host_path):
    absolute_path = os.path.abspath(host_path)
    print(f"Mounting {host_path} as {absolute_path}...")

    return subprocess.run(
        [
            "docker",
            "run",
            "--rm",
            # Add your flags here
            "-v",
            f"{absolute_path}:/app/script.py",
            "grader-base",
            "python3",
            "/app/script.py",
        ],
        stdout=sys.stdout,
        stderr=sys.stderr,
    )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Please provide the path to the student solution.")
        print("Usage: python3 grader_with_basic_isolation.py <student_solution.py>")
        sys.exit(1)

    submission_path = sys.argv[1]

    execute_in_container(submission_path)
