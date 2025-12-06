import subprocess
import sys
import os


def execute_isolated(host_path):
    absolute_path = os.path.abspath(host_path)
    print(f"Mounting {host_path} as {absolute_path}...")

    return subprocess.run(
        [
            "docker",
            "run",
            "--rm",
            "--network",
            "none",
            "--cpus",
            "0.5",
            "--memory",
            "256m",
            "--memory-swap",
            "256m",
            "--pids-limit",
            "64",
            "--ulimit",
            "nofile=64:64",
            "--read-only",
            "--user",
            "1000:1000",
            "--security-opt",
            "no-new-privileges",
            "--tmpfs",
            "/tmp:rw,noexec,nosuid,size=64m",
            "-v",
            f"{absolute_path}:/app/script.py:ro",
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
        print("Usage: python3 isolated_grader.py <student_solution.py>")
        sys.exit(1)

    submission_path = sys.argv[1]

    execute_isolated(submission_path)
