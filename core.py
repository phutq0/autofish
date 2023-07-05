import subprocess

def command(command, replace=False):
    result = subprocess.check_output(command, shell=True)
    output = result.decode("utf-8")
    if replace:
        output = output.replace("\r", "")
    return output