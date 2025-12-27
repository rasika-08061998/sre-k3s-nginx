#!/usr/bin/env python3

import subprocess
import time
import sys

def run(command):
    """
    Execute a system command safely and print output.
    """
    print(f"\n>>> Executing: {command}")
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    stdout, stderr = process.communicate()
    print(stdout)

    if process.returncode != 0:
        print(stderr)
        sys.exit(f"Command failed: {command}")

def main():
    print("=== Python Automation: k3s Installation Started ===")

    run("sudo apt update -y")
    run("sudo apt install -y curl ca-certificates")

    run("curl -sfL https://get.k3s.io | sh -")

    print("Waiting for k3s services to initialize...")
    time.sleep(25)

    run("sudo kubectl get nodes")

    print("=== k3s Installation Completed Successfully ===")

if __name__ == "__main__":
    main()
