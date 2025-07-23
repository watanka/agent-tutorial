import subprocess
import shlex


def execute_command(command):
    try:
        command = command.strip().strip("`")
        command = shlex.split(command)
        result = subprocess.check_output(command, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"
